import asyncio

from github import GitHubClient


async def main():
    async with GitHubClient("eclipse-score") as client:
        teams_data = await client.teams()
        print(teams_data)


if __name__ == "__main__":
    asyncio.run(main())
