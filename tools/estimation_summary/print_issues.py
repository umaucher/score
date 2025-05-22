import asyncio
from dataclasses import dataclass

import src.github_types as gt
from src.github import GitHubClient


@dataclass
class SizeGroup:
    short_name: str
    element_size: float
    issues: list[gt.Issue]


async def main():
    async with GitHubClient("eclipse-score") as client:
        issues: list[gt.Issue] = await client.issues_from_project(6)
        with open("issues.csv", "w") as f:
            f.write("id,title,url,closed,size,status,category,month\n")
            for issue in issues:
                if issue.closed:
                    continue
                if issue.title.startswith("Epic:"):
                    continue
                if issue.custom_fields.get("month", None) is None:
                    continue

                f.write(
                    f"{issue.id},\"{issue.title}\",\"{issue.url}\",{issue.closed},"
                    f"{issue.custom_fields.get('size', 'not estimated')},"
                    f"{issue.custom_fields.get('Status', None)},"
                    f"{issue.custom_fields.get('category', None)},"
                    f"{issue.custom_fields.get('month', None)}\n"
                )



if __name__ == "__main__":
    asyncio.run(main())
