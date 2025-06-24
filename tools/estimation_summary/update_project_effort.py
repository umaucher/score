import asyncio
from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint

import src.github_types as gt
from src.github import GitHubClient

size_to_days = {
    "S (hours...)": 1,
    "M (days...)": 5,
    "L (weeks...)": 12,
    "XL (months... too large!)": 20,
    "not estimated": 5,
    None: 5,
}
size_to_short = {
    "S (hours...)": "S",
    "M (days...)": "M",
    "L (weeks...)": "L",
    "XL (months... too large!)": "XL",
    "not estimated": "N/A",
    None: "N/A",
}


@dataclass
class SizeGroup:
    short_name: str
    element_size: float
    issues: list[gt.Issue]


def aggregate_issue_sizes(issues: list[gt.Issue]) -> list[SizeGroup]:
    size_groups: dict[str, SizeGroup] = dict()
    for issue in issues:
        cat = issue.custom_fields.get("category")
        if cat and (cat.endswith("C++") or cat.endswith("Rust")):
            continue

        size_str = issue.custom_fields.get("size", "not estimated")
        short_name = size_to_short[size_str]

        size = size_to_days[size_str]
        if issue.custom_fields.get("Status") == "In Progress":
            suffix = " (in progress)"
            size = size / 2
        else:
            suffix = ""

        short_name = size_to_short[size_str] + suffix

        if short_name not in size_groups:
            size_groups[short_name] = SizeGroup(
                short_name=short_name,
                element_size=size,
                issues=[],
            )

        size_groups[short_name].issues.append(issue)

    return list(size_groups.values())


async def main():
    async with GitHubClient("eclipse-score") as client:
        issues: list[gt.Issue] = await client.issues_from_project(6)

        # Group issues by month and size
        data = defaultdict(lambda: list())
        for issue in issues:
            if not issue.closed and "is_parent" not in issue.custom_fields:
                month = issue.custom_fields.get("month", "unplanned")
                data[month].append(issue)

        # Collect summary
        summary = []
        for month in sorted(data.keys()):
            sizes = aggregate_issue_sizes(data[month])
            month_total = 0

            month_info: list[str] = []
            for size_group in sorted(sizes, key=lambda g: g.short_name):
                month_total += size_group.element_size * len(size_group.issues)
                month_info.append(
                    f"{len(size_group.issues)}x{size_group.short_name} ({size_group.element_size})"
                )

            summary.append(f"{month} 📅: {month_total} days - {', '.join(month_info)}")

        summary_str = "Without C++ and Rust:\n" + "\n".join(summary)
        print(f"Setting summary:\n{summary_str}")
        await client.set_project_description(6, summary_str)


if __name__ == "__main__":
    asyncio.run(main())
