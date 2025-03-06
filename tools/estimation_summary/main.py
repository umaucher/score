import asyncio
from collections import defaultdict

import github_types as gt
from github import GitHubClient

size_to_days = {
    "size:S (hours...)": 1,
    "size:M (days...)": 5,
    "size:L (weeks...)": 12,
    "size:XL (months... too large!)": 20,
    None: 5,
}
size_to_short = {
    "size:S (hours...)": "S",
    "size:M (days...)": "M",
    "size:L (weeks...)": "L",
    "size:XL (months... too large!)": "XL",
    None: "N/A",
}


async def main():
    async with GitHubClient("eclipse-score") as client:
        issues: list[gt.Issue] = await client.issues_from_project(6)

        # Group issues by month and size
        data = defaultdict(lambda: defaultdict(lambda: list()))
        for issue in issues:
            if not issue.closed and "is_parent" not in issue.custom_fields:
                month = issue.custom_fields.get("month", "unplanned")
                size = issue.custom_fields.get("size", None)
                data[month][size].append(issue)

        # Collect summary
        summary = []
        for month in sorted(data.keys()):
            total = 0

            per_size = []
            for size, issues in data[month].items():
                total += len(issues) * size_to_days[size]
                per_size.append(f"{len(issues)}x{size_to_short[size]}")

            summary.append(f"{month} 📅: {total} days ({', '.join(per_size)})")

        await client.set_project_description(6, "\n".join(summary))


if __name__ == "__main__":
    asyncio.run(main())
