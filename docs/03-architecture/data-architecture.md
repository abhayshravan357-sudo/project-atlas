# Data Architecture — Project Atlas

## Data stores

| Store | Location | Format | Purpose |
|-------|----------|--------|---------|
| Git repository | .git | Git objects | Source of truth for all branches and worktrees |
| Worktrees | project-atlas-worktrees/<domain>/ | Filesystem | Isolated working directories per domain |
| Knowledge base | docs/knowledge-base/ | Markdown, CSV, JSON | Synthesized findings from approved reports |
| Research reports | docs/research/<domain>/ | Markdown | Agent deliverables |
| Management docs | docs/09-management/ | Markdown | Dashboard, task register, decisions, changelog |
| Technology docs | docs/02-technology/ | Markdown | Technology stack documentation |
| Overview docs | docs/00-overview/ | Markdown | Vision, problem, goals, scope, features, glossary |
| Requirements docs | docs/01-requirements/ | Markdown | Functional and non-functional requirements |

## Data flow

1. **Objective input**: Owner provides a research objective (text).
2. **Domain decomposition**: Objective split into domain list (JSON-like state).
3. **Branch/worktree creation**: Git creates branches and worktree directories.
4. **Worker execution**: Worker reads assignment, writes report file in worktree.
5. **Report collection**: Manager reads report files from worktrees.
6. **Synthesis**: Approved reports combined into knowledge base Markdown files.
7. **Merge**: Approved branch merged into main.

## Data retention

- All research branches are preserved (not deleted) for audit history.
- Worktrees are preserved for reference; may be removed after merge with Manager approval.
- All reports and documentation are version-controlled in Git.

## Data classification

| Classification | Description | Handling |
|---------------|-------------|----------|
| FACT | Claim supported by credible evidence with source link | Cited in report |
| INTERPRETATION | Conclusion derived from evidence | Labeled in report |
| HYPOTHESIS | Idea requiring validation | Labeled in report |
| PROPOSAL | Suggested direction for the project | Labeled in report |

## Status

Proposed — no data implementation exists yet beyond Git repository and documentation files.
