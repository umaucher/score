import asyncio
import subprocess

from github import GitHubClient

# GitHub repository details
ORG = "eclipse-score"
REPO = "score"

# Get the last commit for each .rst file
files = (
    subprocess.run(
        "git ls-files '*.rst' | while read file; do echo \"$(git log -1 --format='%H' -- $file) $file\"; done",
        shell=True,
        capture_output=True,
        text=True,
    )
    .stdout.strip()
    .split("\n")
)

# Generate GraphQL query
query = f"""query {{
    rateLimit {{
        limit
        remaining
        used
        resetAt
        cost
    }}
  repository(owner: "{ORG}", name: "{REPO}") {{
"""
for i, line in enumerate(files):
    commit_hash, file_path = line.split(" ", 1)
    query += f'    commit{i}: object(expression: "{commit_hash}") {{\n'
    query += """                  ... on Commit {
        associatedPullRequests(first:10) {
            nodes {
                author {
                    login
                }
                approver: reviews(first:100, states: APPROVED) {
                    nodes {
                        state
                        author {
                            login
                        }
                    }
                }
                reviewer: reviews(first:100, states: [COMMENTED, CHANGES_REQUESTED, DISMISSED]) {
                    nodes {
                        state
                        author {
                            login
                        }
                    }
                }
            }
        }
      }
    }\n"""
query += "  }\n}"

print(query)


async def main():
    async with GitHubClient("eclipse-score") as client:
        teams_data = await client.teams()
        print(teams_data)


if __name__ == "__main__":
    asyncio.run(main())
