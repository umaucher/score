from pathlib import Path
from pprint import pprint

import github_types
from github_basics import GitHubClient_Basic, get_query


def _decode(project: int, item: dict):
    content = item.get("content")
    if not content:
        # It's probably a pull request and not an issue
        # TODO: how to query only issues?
        return None

    issue = github_types.Issue(
        id=content["number"],
        # v2: id=content.numb
        title=content["title"],
        url=content["url"],
        closed=content["closed"],
        milestone=content["milestone"]["title"] if content["milestone"] else None,
        custom_fields={},
    )

    # v2:
    # if item.fieldValues:
    #     for f in item.fieldValues.nodes:

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


async def run_mutation(
    client: GitHubClient_Basic, org: str, project_number: int, readme: str
):
    """Will return a dict with the project name and new readme."""
    # Note: would be nice if we had a code generator that would have generated
    # an appropriate dataclass for the return type of this query...

    # TODO: cache id
    result1 = await client._execute(
        query=get_query("get_project_id"),
        variable_values={
            "org": org,
            "projectNumber": project_number,
        },
    )
    # pprint(id) -> {'organization': {'projectV2': {'id': 'PVT_kwDOCy9hX84AzmuL'}}}
    # result1.organization.projectV2.id
    id = result1["organization"]["projectV2"]["id"]
    assert isinstance(id, str), result1

    result2 = await client._execute(
        query=get_query(Path(__file__).stem),
        variable_values={
            "org": org,
            "projectId": id,
            "readme": readme,
        },
    )

    print("Result:")
    pprint(result2)
    actual_readme = result2["updateProjectV2"]["projectV2"]["readme"]
    assert readme == actual_readme, actual_readme
    return result2
