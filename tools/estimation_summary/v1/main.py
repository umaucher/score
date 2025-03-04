import asyncio
from collections import defaultdict
from pprint import pprint

import github_types as gt
from github import GitHubClient

size_to_days = {
    "size:S (hours...)": 1,
    "size:M (days...)": 5,
    "size:L (weeks...)": 12,
    "size:XL (months... too large!)": 20,
    "not estimated": 5,
}
size_to_short = {
    "size:S (hours...)": "S",
    "size:M (days...)": "M",
    "size:L (weeks...)": "L",
    "size:XL (months... too large!)": "XL",
    "not estimated": "<not estimated>",
}


async def main():
    async with GitHubClient("eclipse-score") as client:
        issues: list[gt.Issue] = await client.issues_from_project(6)

        # Group issues by month and size
        data = defaultdict(lambda: defaultdict(lambda: list()))
        for issue in issues:
            if not issue.closed and "is_parent" not in issue.custom_fields:
                month = issue.custom_fields.get("month", "unplanned")
                size = issue.custom_fields.get("size", "not estimated")
                data[month][size].append(issue)

        # Print summary
        for month in sorted(data.keys()):
            total = 0

            per_size = []
            for size, issues in data[month].items():
                total += len(issues) * size_to_days[size]
                per_size.append(f"{len(issues)}x{size_to_short[size]}")

            summary = f"{month} 📅: {total} days ({', '.join(per_size)})"
            print(summary)

            # await client.set_project_single_select_field_description(
            #     project_number=6,
            #     field="month",
            #     field_value=month,
            #     new_description=summary,
            # )


if __name__ == "__main__":
    asyncio.run(main())
