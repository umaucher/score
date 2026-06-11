# AI Agent Extension Guide — eclipse-score

This document defines the rules for extending AI agent context across all eclipse-score
repositories. Read this before adding any agent customization file.

## Guiding Principles

1. **Single point of truth** — never duplicate information that already exists in code or
   docs. Agent files *point* to sources; they do not repeat them.
2. **Minimal always-on context** — `AGENTS.md` carries only what an agent cannot infer
   from reading the repo. Everything else is on-demand.
3. **Portability** — prefer `.agents/` for cross-tool assets (Copilot, Claude Code,
   Codex, ...). Use `.github/` only for Copilot-specific primitives.
4. **Personal extensions belong in `~/.agents/`** — never commit personal workflows or
   knowledge-base skills to a repo.

## Folder Layout & Tool Support

```
<repo>/
├── AGENTS.md                        # Cross-tool entry point (root preferred)
│                                    # Recognized by: Copilot, Claude Code, Codex
├── CLAUDE.md                        # Claude Code specific overrides (if needed)
│
├── .agents/                         # Cross-tool, portable layer
│   ├── skills/<name>/SKILL.md       # On-demand skills (Copilot + Claude Code)
│   └── docs/                        # Reference docs loaded on demand by agents
│
└── .github/                         # Copilot-specific primitives
    ├── instructions/*.instructions.md   # applyTo-scoped or on-demand instructions
    ├── agents/*.agent.md                # Custom agent personas with tool restrictions
    ├── prompts/*.prompt.md              # Slash-command prompts
    └── docs/                            # On-demand reference docs (API notes, etc.)
```

### What goes where

| Asset | Location | Auto-loaded? | Cross-tool? |
|-------|----------|-------------|-------------|
| Repo overview, key facts | `AGENTS.md` (root) | ✅ always | ✅ |
| Generic shared skills | `score/.agents/skills/<name>/` | on-demand | ✅ |
| Feature-specific skills | `<feature>/.agents/skills/<name>/` | on-demand | ✅ |
| File-scoped coding rules | `.github/instructions/<name>.instructions.md` | via `applyTo` | Copilot only |
| Custom agent personas | `.github/agents/<name>.agent.md` | user-invoked | Copilot only |
| Slash-command prompts | `.github/prompts/<name>.prompt.md` | user-invoked | Copilot only |
| Reference data (IDs, snippets) | `.github/docs/` or `.agents/docs/` | on-demand | depends |
| Personal workflows | `~/.agents/skills/` | on-demand | ✅ |

## Hierarchy Between Repos

When multiple repos are open in the same workspace (e.g. `score` + `persistency`):

- **`score/AGENTS.md`** provides org-wide context (always active for all repos in workspace)
- **`<feature>/AGENTS.md`** provides feature-specific context, references score for the rest
- Feature `AGENTS.md` must include:
  ```
  > When working in this repo alongside score, score/AGENTS.md is also active.
  > For standalone use, see: https://github.com/eclipse-score/score/blob/main/AGENTS.md
  ```

## Adding a New Skill

1. Decide scope: generic (all teams) → `score/.agents/skills/`, feature-specific → `<feature>/.agents/skills/`
2. Create folder: `.agents/skills/<skill-name>/SKILL.md`
3. Required frontmatter:
   ```yaml
   ---
   name: skill-name          # must match folder name, lowercase-hyphenated
   description: 'What it does. Use when: ... triggers ...'
   ---
   ```
4. Keep `SKILL.md` under 500 lines; put detail in `./references/` subfolder
5. Do not vendor a skill that already exists in `score/.agents/skills/`

## Adding a New Instruction (Copilot only)

1. Place in `.github/instructions/<name>.instructions.md`
2. Use `applyTo` for file-scoped rules (e.g. `applyTo: "**/*.rs"`)
3. Use `description:` for on-demand task rules (e.g. safety review checklist)
4. Never use `applyTo: "**"` unless truly universal — it loads on every request

## Adding Reference Documentation

- GitHub API IDs, GraphQL snippets, external system IDs → `.github/docs/`
- Anything an agent needs to *act* (procedures, runbooks) → `.agents/docs/`
- Link from `AGENTS.md` — do not repeat content inline

The same rules apply to any domain: git conventions, CI/CD runbooks, release procedures, etc.
If a topic is **org-wide**, the reference doc lives in `score/` and feature repos link to it.
If a topic is **feature-specific**, the doc lives in the feature repo and may reference the score doc for shared context.

When adding a new reference doc:

1. Decide scope: org-wide → `score/`, feature-specific → `<feature>/`
2. Decide type: static IDs / external data → `.github/docs/`, agent procedures / runbooks → `.agents/docs/`
3. Link to it from `AGENTS.md` under an **On-Demand References** table
4. If a feature doc extends an org-wide one, reference the score doc rather than duplicating content

## Feature Repo Checklist

When setting up a new feature repo for agent use:

- [ ] `AGENTS.md` at repo root with: FT discussion number → score, ASIL level →
      `project_config.bzl`, `reference_integration` relationship
- [ ] `.agents/skills/` — only feature-specific skills (created when needed)
- [ ] `.agents/docs/` — feature-specific runbooks/procedures (created when needed)
- [ ] `.github/docs/` — feature-specific reference data, e.g. `score_github_api.md` (created when needed)
- [ ] `.github/instructions/` — Copilot-only scoped rules (created when needed)
- [ ] `.github/agents/` — Copilot-only custom agents (created when needed)
- [ ] `.github/prompts/` — Copilot-only prompts (created when needed)
