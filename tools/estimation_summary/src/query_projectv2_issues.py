import functools
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pprint import pprint

sys.path.insert(0, ".")
from github_basics import GitHubClient_Basic, parse

# TODO: maybe this is not "github", but "issues_from_project"?
# We'll see once we add more functionality to the GitHubClient class.


@functools.cache
def _query():
    return parse("""
    query($org: String!, $projectNumber: Int!, $cursor: String) {
        rateLimit {
            limit
            cost
            remaining
            resetAt
        }
        organization(login: $org) {
            projectV2(number: $projectNumber) {
                items(first: 50, after: $cursor) {
                    # Type: ProjectV2ItemConnection!
                    totalCount
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                    nodes {
                        # Type: ProjectV2Item
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
                                # Union: ProjectV2ItemFieldValue
                                # Can be one of those:
                                # ProjectV2ItemFieldDateValue
                                # ProjectV2ItemFieldIterationValue
                                # ProjectV2ItemFieldLabelValue
                                # ProjectV2ItemFieldMilestoneValue
                                # ProjectV2ItemFieldNumberValue
                                # ProjectV2ItemFieldPullRequestValue
                                # ProjectV2ItemFieldRepositoryValue
                                # ProjectV2ItemFieldReviewerValue
                                # ProjectV2ItemFieldSingleSelectValue
                                # ProjectV2ItemFieldTextValue
                                # ProjectV2ItemFieldUserValue

                                ... on ProjectV2ItemFieldSingleSelectValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            id
                                            name
                                        }
                                    }
                                    name
                                }
                                ... on ProjectV2ItemFieldTextValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            id
                                            name
                                        }
                                    }
                                    text
                                }
                                ... on ProjectV2ItemFieldDateValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            id
                                            name
                                        }
                                    }
                                    date
                                }
                                ... on ProjectV2ItemFieldIterationValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            id
                                            name
                                        }
                                    }
                                    title
                                }
                                ... on ProjectV2ItemFieldNumberValue {
                                    field {
                                        ... on ProjectV2FieldCommon {
                                            id
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

def _decode(project: int, item: dict):
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

        name: str = f["field"]["name"]
        # TODO: id is not used... is the name truly unique?
        _id: str = f["field"]["id"]

        if "name" in f:
            val = f["name"]
        elif "text" in f:
            val = f["text"]
        elif "date" in f:
            val = f["date"]
        elif "title" in f:
            val = f["title"]
        elif "number" in f:
            val = f["number"]
        else:
            raise ValueError(f"Unknown field value: {f}")

        issue.custom_fields[name] = val

    return issue

async def run_query(self, project_number: int):
    """
    Get all issues within the project.

    Warning: result is cached for 1 hour.
    Changes to GitHub will not be reflected.
    """

    issues = await self.fetch_all_elements(
        query=_query(),
        variable_values={
            "org": self.org,
            "projectNumber": project_number,
        },
        path_to_elements=["organization", "projectV2", "items"],
        decoder=lambda item: _decode(project_number, item),
    )

    print(f"✅ {len(issues)} issues fetched")
    return issues
