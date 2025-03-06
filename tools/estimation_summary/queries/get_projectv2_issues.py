import functools
from pathlib import Path

import github_types
from github_basics import GitHubClient_Basic, parse


@functools.cache
def _query():
    query = Path(__file__).with_suffix(".graphql").read_text()
    return parse(query)


def _decode(project: int, node: dict):
    content = node.get("content")
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

    for f in node.get("fieldValues", {}).get("nodes", []):
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


async def run_query(client: GitHubClient_Basic, project_number: int):
    """
    Get all issues within the project.

    Warning: result is cached for 1 hour.
    Changes to GitHub will not be reflected.
    """

    issues: list[github_types.Issue] = await client.fetch_all_elements(
        query=_query(),
        variable_values={
            "org": client.org,
            "projectNumber": project_number,
        },
        path_to_elements=["organization", "projectV2", "items"],
        decoder=lambda item: _decode(project_number, item),
    )

    print(f"✅ {len(issues)} issues fetched")
    return issues
