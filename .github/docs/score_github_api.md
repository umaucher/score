# Eclipse Score GitHub API Notes

Useful IDs and GraphQL snippets for automating tasks against the eclipse-score GitHub organization.

> **Repo-specific notes** (category IDs, discussion lists per feature team, etc.) live in the
> `.github/docs/score_github_api.md` of each respective repository and reference this file.

## Organization

- Login: `eclipse-score`
- Node ID: `O_kgDOCy9hXw`
- Org-level discussion URLs: `https://github.com/orgs/eclipse-score/discussions/<number>`
- Org discussions are physically stored in the **`eclipse-score/score`** repository

## Prerequisites

- [GitHub CLI (`gh`)](https://cli.github.com/) installed and authenticated:
  ```bash
  gh auth login --hostname github.com
  # Token needs write:discussion scope for mutations
  ```

## Useful GraphQL Snippets

### List all discussions in a category

```bash
gh api graphql -f query='
{
  repository(owner: "eclipse-score", name: "score") {
    discussions(first: 100, categoryId: "<CATEGORY_ID>") {
      nodes { number title closed id }
    }
  }
}'
```

### Close a discussion

```bash
gh api graphql -f query='
mutation($id: ID!) {
  closeDiscussion(input: {discussionId: $id}) {
    discussion { number closed }
  }
}' -f id=<NODE_ID>
```

### Reopen a discussion

```bash
gh api graphql -f query='
mutation($id: ID!) {
  reopenDiscussion(input: {discussionId: $id}) {
    discussion { number closed }
  }
}' -f id=<NODE_ID>
```

### Bulk close all open discussions in a category (with exclusions)

`KEEP` is a comma-separated list of discussion numbers to leave open. Omit to close all.

```bash
KEEP=<NUMBER>[,<NUMBER>,...]   # e.g. KEEP=2518,116
CATEGORY=<CATEGORY_ID>

gh api graphql -f query='
{
  repository(owner: "eclipse-score", name: "score") {
    discussions(first: 100, categoryId: "'"$CATEGORY"'") {
      nodes { number title closed id }
    }
  }
}' | python3 -c "
import json, sys, subprocess, os
nodes = json.load(sys.stdin)['data']['repository']['discussions']['nodes']
keep = {int(x) for x in os.environ.get('KEEP', '').split(',') if x.strip()}
mutation = 'mutation(\$id: ID!) { closeDiscussion(input: {discussionId: \$id}) { discussion { number title closed } } }'
for n in nodes:
    if not n['closed'] and n['number'] not in keep:
        r = subprocess.run(['gh','api','graphql','-f',f'query={mutation}','-f',f'id={n[\"id\"]}'],
                           capture_output=True, text=True)
        d = json.loads(r.stdout)
        print(d['data']['closeDiscussion']['discussion'])
    else:
        print(f'skipped #{n[\"number\"]} ({n[\"title\"][:40]})')
"
```
