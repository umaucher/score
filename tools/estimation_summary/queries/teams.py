from pathlib import Path
from pprint import pprint

import github_types
from github_basics import GitHubClient_Basic, get_query


async def run_query(
    client: GitHubClient_Basic
):
    """Will return a dict with the project name and new readme."""
    # Note: would be nice if we had a code generator that would have generated
    # an appropriate dataclass for the return type of this query...

    # TODO: cache id
    result1 = await client.fetch_all_elements(
        query=get_query("get_teams"),
        variable_values={
            "org": client.org,
        },
        decoder=lambda data: data,
        path_to_elements=["organization", "teams"],
    )
    pprint(result1)
    return result1
