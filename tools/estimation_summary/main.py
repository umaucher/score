from github import GitHubClient, Issue


async def main():
    async with GitHubClient("eclipse-score") as client:
        issues: list[Issue] = await client.issues_from_project(6)
        print(f"Found {len(issues)} issues")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
