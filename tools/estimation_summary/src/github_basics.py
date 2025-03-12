import functools
import os
import sys
import urllib.request
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
    import graphql
    from gql import Client
    from gql.transport.aiohttp import AIOHTTPTransport
except ImportError:
    sys.exit(
        "❌ Missing required module 'gql'. "
        "Please install it with 'pip install gql[all]'."
    )

# TODO: split this class into "lower level" and "higher level".
# Mostly for improved caching, as it includes the file hash!

# Set up DiskCache
cache = dc.Cache(Path("/tmp/diskcache"))

@memoize(cache, expire=timedelta(days=1))
def _download(
    url: str,
):
    try:
        path, _ = urllib.request.urlretrieve(url)
        return Path(path).read_text()
    except Exception as e:
        sys.exit(f"❌ Failed to download {url}: {str(e)}")

@functools.cache
def get_query(name):
    file = Path(__file__).parent / "queries" / f"{name}.graphql"
    query = file.read_text()
    return parse(query)

def _load_github_graphql_schema():
    """
    Download the GitHub GraphQL schema and parse it.

    Note: GraphQL also supports introspection queries to fetch the schema,
    but this way it can be downloaded and cached locally for better performance.
    """
    schema = _download(
        "https://docs.github.com/public/fpt/schema.docs.graphql",
    )

    # Store schema for LSP
    file = Path(__file__).parent / ".schema.docs.graphql"
    if not file.exists():
        file.write_text(schema)

    return graphql.build_ast_schema(graphql.parse(schema))

GITHUB_SCHEMA = _load_github_graphql_schema()


def parse(query: str):
    """
    Validates a GraphQL query against GITHUB_SCHEMA.

    This function checks the query for errors using the GITHUB_SCHEMA. If any errors are
    found, the function will terminate the program and display the errors. This
    pre-validation is especially useful when the query is modified, as it prevents
    unnecessary API connections with invalid queries.
    """
    parsed = graphql.parse(query)
    errors = graphql.validate(GITHUB_SCHEMA, parsed)
    if errors:
        sys.exit(f"❌ Invalid GitHub GraphQL query: {errors}")
    return parsed


class GitHubClient_Basic:
    def __init__(self, org: str, token: str | None = None):
        """
        Hint: you *must* use this class as a context manager.

        Args:
          token: will default to the GITHUB_TOKEN environment variable if not provided.
        """

        self.org = org

        if not token:
            load_dotenv(verbose=True)
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

    # @memoize(cache, expire=timedelta(hours=1), ignore_self=True)
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
            #v2: cursor = result.pageInfo.endCursor

        return nodes

    async def fetch_all_elements(self, query, variable_values, path_to_elements, decoder):
        """
        Fetch all elements from a paginated query.
        """

        data: list = []

        for node in await self._execute_paginated(
            query,
            variable_values,
            path_to_pageInfo=path_to_elements,
        ):
            if d := decoder(node):
                data.append(d)

        return data
