import asyncio

import graphql_client

async def _execute_paginated(client: graphql_client.Client, query: str, variable_values: dict[str, Any], path_to_pageInfo: list[str]):
    ... # similar to v1

async def get_issues(client: graphql_client.Client, org: str, project_number: int):
    cursor = None
    # result +=
    await client.project_v_2_issues("eclipse-score", 6, cursor)
    # if results contains pageInfo...
    # cursor = results.pageInfo.endCursor
    # iterate...

async def main():
    async with graphql_client.Client(url = "http://my-client.com") as client:
        result =
        # `result` will be an instance of Pydantic model representing the result of
        # `GetHello` query!
        print(result.hello)

if __name__ == "__main__":
    asyncio.run(main())
