import functools
import os
import sys
import urllib.request
from dataclasses import dataclass, field
from datetime import timedelta
from pathlib import Path
from typing import Any

import diskcache as dc

sys.path.insert(0, ".")
from diskcache_decorator import memoize

try:
    from dotenv import load_dotenv
except ImportError:
    sys.exit(
        "❌ Missing required module 'python-dotenv'. "
        "Please install it with 'pip install python-dotenv'."
    )

try:
    from gql import Client
    from gql.transport.aiohttp import AIOHTTPTransport
    from graphql import build_ast_schema, parse, validate
except ImportError:
    sys.exit(
        "❌ Missing required module 'gql'. "
        "Please install it with 'pip install gql[all]'."
    )

# TODO: split this class into "lower level" and "higher level".
# Mostly for improved caching, as it includes the file hash!

# Set up DiskCache
cache = dc.Cache(Path("/tmp/diskcache"))


@dataclass
class Issue:
    id: int
    title: str
    url: str
    closed: str
    milestone: str | None
    custom_fields: dict[str, str] = field(default_factory=dict)


@memoize(cache, expire=timedelta(days=1))
def _download(
    url: str,
):
    try:
        path, _ = urllib.request.urlretrieve(url)
        return Path(path).read_text()
    except Exception as e:
        sys.exit(f"❌ Failed to download {url}: {str(e)}")


def _load_github_graphql_schema():
    """
    Download the GitHub GraphQL schema and parse it.

    Note: GraphQL also supports introspection queries to fetch the schema,
    but this way it can be downloaded and cached locally for better performance.
    """
    schema = _download(
        "https://docs.github.com/public/fpt/schema.docs.graphql",
    )
    return build_ast_schema(parse(schema))

# TODO: when everything is cached, there is no need to load the schema.
# Can we lazy load it?
GITHUB_SCHEMA = _load_github_graphql_schema()


def _validate_github_query(query):
    """
    Validates a GraphQL query against GITHUB_SCHEMA.

    This function checks the query for errors using the GITHUB_SCHEMA. If any errors are
    found, the function will terminate the program and display the errors. This
    pre-validation is especially useful when the query is modified, as it prevents
    unnecessary API connections with invalid queries.
    """
    errors = validate(GITHUB_SCHEMA, query)
    if errors:
        sys.exit(f"❌ Invalid GitHub GraphQL query: {errors}")


@functools.cache
def _issues_from_project_query():
    query = parse("""
    query($org: String!, $projectNumber: Int!, $cursor: String) {
        rateLimit {
            limit
            cost
            remaining
            resetAt
        }
        organization(login: $org) {
            projectV2(number: $projectNumber) {
                number # sanity check, same as projectNumber
                items(first: 50, after: $cursor) {
                    totalCount
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                    nodes {
                        id
                        content {
                            ... on Issue {
                                number
                                title
                                url
                                closed # issues can only be open or closed!
                                milestone {
                                    title
                                }
                            }
                            # Info: Other types are DraftIssue and PullRequest
                        }
                        fieldValues(first: 99) {
                            nodes {
                                ... on ProjectV2ItemFieldSingleSelectValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            name
                                        }
                                    }
                                    name
                                }
                                ... on ProjectV2ItemFieldTextValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            name
                                        }
                                    }
                                    text
                                }
                                ... on ProjectV2ItemFieldDateValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            name
                                        }
                                    }
                                    date
                                }
                                ... on ProjectV2ItemFieldIterationValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            name
                                        }
                                    }
                                    title
                                }
                                ... on ProjectV2ItemFieldNumberValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            name
                                        }
                                    }
                                    number
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    """)
    _validate_github_query(query)
    return query


class GitHubClient:
    def __init__(self, org: str, token: str | None = None):
        """
        Hint: you *must* use this class as a context manager.

        Args:
          token: will default to the GITHUB_TOKEN environment variable if not provided.
        """

        self.org = org

        if not token:
            load_dotenv()
            self.token = os.getenv("GITHUB_TOKEN")

    async def __aenter__(self):
        transport = AIOHTTPTransport(
            url="https://api.github.com/graphql",
            headers={"Authorization": f"Bearer {self.token}"},
            ssl=True,
        )

        self.client = Client(transport=transport, schema=GITHUB_SCHEMA)
        self.session = None
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.client.close_async()
            print("🔌 Disconnected from GitHub GraphQL API")

    async def _session(self):
        """Lazy session creation."""
        if not self.session:
            self.session = await self.client.connect_async(reconnecting=True)
            print("🔌 Connected to GitHub GraphQL API")
        return self.session

    async def _execute(self, query, variable_values):
        session = await self._session()
        return await session.execute(query, variable_values=variable_values)

    def _check_rate_limit(self, result):
        # Very conservative rate limit warning for now
        rateLimit = result.get("rateLimit", None)
        if rateLimit:
            percent = rateLimit["remaining"] / rateLimit["limit"] * 100
            if percent < 80:
                print(
                    f"⚠️ Rate limit: {percent}% remaining. "
                    f"Reset at {rateLimit['resetAt']}"
                )

    @memoize(cache, expire=timedelta(hours=1), ignore_self=True)
    async def _execute_paginated(
        self, query, variable_values: dict[str, Any], path_to_pageInfo: list[str]
    ):
        """
        Execute a query and handle pagination.

        Args:
            query: Must contain exactly one "pageInfo" object.
            variable_values: the variables to pass to the query
            path_to_pageInfo: a list of keys to reach the "pageInfo" object
        """
        # TODO: can we get path_to_pageInfo from the query by parsing it?

        nodes = []
        cursor = None
        while True:
            result = await self._execute(query, {**variable_values, "cursor": cursor})
            self._check_rate_limit(result)

            for p in path_to_pageInfo:
                result = result[p]

            for node in result["nodes"]:
                nodes.append(node)

            if not result["pageInfo"]["hasNextPage"]:
                break

            cursor = result["pageInfo"]["endCursor"]

        return nodes

    async def issues_from_project(self, project_number: int):
        """
        Get all issues within the project.

        Warning: result is cached for 1 hour.
        Changes to GitHub will not be reflected.
        Changes to this code itself will also not be reflected!
        """

        issues: list[Issue] = []

        for node in await self._execute_paginated(
            _issues_from_project_query(),
            {
                "org": self.org,
                "projectNumber": project_number,
            },
            path_to_pageInfo=["organization", "projectV2", "items"],
        ):
            issue = self._parse_issue(node)
            if issue:
                issues.append(issue)

        print(f"✅ {len(issues)} issues downloaded")
        return issues

    def _parse_issue(self, item: dict):
        content = item.get("content")
        if not content:
            # It's probably a pull request and not an issue
            # TODO: how to query only issues?
            return None

        issue = Issue(
            id=content["number"],
            title=content["title"],
            url=content["url"],
            closed=content["closed"],
            milestone=content["milestone"]["title"] if content["milestone"] else None,
        )

        for f in item.get("fieldValues", {}).get("nodes", []):
            if not f:
                # TODO: what type is missing in the query?
                continue

            name = f["field"]["name"]
            if "name" in f:
                issue.custom_fields[name] = f["name"]
            elif "text" in f:
                issue.custom_fields[name] = f["text"]
            elif "date" in f:
                issue.custom_fields[name] = f["date"]
            elif "title" in f:
                issue.custom_fields[name] = f["title"]
            elif "number" in f:
                issue.custom_fields[name] = f["number"]
        return issue
