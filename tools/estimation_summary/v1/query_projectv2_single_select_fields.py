import functools
import sys

sys.path.insert(0, ".")
import github_basics
import github_types


@functools.cache
def _query():
    return github_basics.parse("""
    query($org: String!, $projectNumber: Int!, $cursor: String) {
        rateLimit {
            limit
            cost
            remaining
            resetAt
        }
        organization(login: $org) {
            projectV2(number: $projectNumber) {
                fields(first: 50, after: $cursor) {
                    # Type: ProjectV2FieldConfigurationConnection!
                    totalCount
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                    nodes {
                        ... on ProjectV2SingleSelectField {
                            id
                            name
                            options {
                                # Type: ProjectV2SingleSelectFieldOption
                                color
                                description
                                descriptionHTML
                                id
                                name
                                nameHTML
                            }
                        }
                    }
                }
            }
        }
    }
    """)

async def run_query(github: github_basics.GitHubClient_Basic, project_number: int):
    for node in await github._execute_paginated(
        query=_query(),
        variable_values={
            # TODO: can GitHubClient automatically provide the org?
            # Or should it not be in the client at all?
            "org": github.org,
            "projectNumber": project_number,
        },
        path_to_pageInfo=["organization", "projectV2", "fields"],
    ):
        # TODO: this is a 1:1 mapping. Any way to make it more generic?
        yield github_types.SingleSelectField(
            id=node["id"],
            name=node["name"],
            options=[
                github_types.SingleSelectFieldOption(
                    id=option["id"],
                    name=option["name"],
                    nameHTML=option["nameHTML"],
                    color=option["color"],
                    description=option["description"],
                    descriptionHTML=option["descriptionHTML"],
                )
                for option in node["options"]
            ],
        )
