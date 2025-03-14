from pathlib import Path
from pprint import pprint

import src.github_types
from src.github_basics import GitHubClient_Basic, get_query


async def run_query(
    client: GitHubClient_Basic
):
    """Will return a dict with the project name and new readme."""
    # Note: would be nice if we had a code generator that would have generated
    # an appropriate dataclass for the return type of this query...

    # TODO: cache id
    result1 = await client._execute(
        query=get_query("commits"),
        variable_values={
        },
    )
    pprint(result1)
    return result1
