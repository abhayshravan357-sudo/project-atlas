# Development Tools — Project Atlas

| Tool | Purpose | Why needed | Where used |
|------|---------|------------|------------|
| Git | Version control | Source of truth, branch-per-domain, clean main | All development |
| git worktree | Isolated working directories per domain | Agent isolation, no file conflicts | Agent workspaces |
| Python venv | Virtual environments | Isolated dependency installation | Development environment |
| pip | Package manager | Install Python packages | Development environment |
| pytest | Test runner | Run unit and integration tests | tests/ |
| Mermaid | Diagramming | Architecture and workflow diagrams | docs/ |
| Markdown | Documentation format | Primary documentation format | docs/ |

## Notes
- Git and git worktrees are already in use (research cycles 1-3).
- No additional tools installed yet.
- Tools are kept minimal to avoid unnecessary complexity.

## Status: Git/git worktree implemented; others proposed
