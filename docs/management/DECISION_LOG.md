# Decision Log — Project Atlas

Important decisions, reasoning, alternatives, and evidence.

## Decisions

| ID | Date | Decision | Reasoning | Alternatives Considered | Evidence |
|----|------|----------|-----------|-------------------------|----------|
| D-001 | 2026-10-30 | Research-first workflow; no application code in cycle 1 | Repository is empty; priority is knowledge base before implementation | Implement a prototype first | Repository inspection (README placeholder, single commit) |
| D-002 | 2026-10-30 | Seven initial research domains for cycle 1 | Covers fundamentals through critical analysis; broad discovery | Single deep dive on one technology | Project Atlas objective (explore many directions) |
| D-003 | 2026-10-31 | Use isolated Git worktrees per research domain for parallel isolation | Keeps main clean; no file conflicts between agents; audit trail via git | Multiple clones; single shared working dir | Git worktree inspection; branch isolation requirement |
| D-004 | 2026-10-31 | Main Agent executes research directly (subagent `task` tool aborted initially; verified working via test session) | `task` subagent spawning returned errors for cycle 2; test session `ses_e6f9f45f7ffeRYELpsJtggMI2r` returned SUBAGENT_READY but subsequent spawns aborted | Spawn specialist agents via `task` | Tool execution results |
| D-005 | 2026-10-31 | Use worktrees without subagents per user direction ("not subagents", "create worktree") | Independent subagent execution not reliably available; Manager produces deliverables into worktrees | Launch independent subagents | User instruction |
| D-006 | 2026-10-31 | Cycle 2 technology recommendation: LangGraph primary, ADK secondary, AutoGen not recommended | Graph model with cycles + persistence + native human-in-the-loop fits research cycle best | Single framework commitment | Agent I Report — Cycle 2 Technology Comparison |
| D-007 | 2026-10-31 | Cycle 2 integration recommendation: adopt MCP for tool access; do not adopt A2A in cycle 2 | MCP is emerging with growing server ecosystem; A2A is very early with few implementations | Adopt both / neither | Agent J Report — Cycle 2 Integration Protocols |

## Pending Decisions

- Cycle 3 deep-dive targets: to be determined after cycle 2 synthesis (likely feasibility prototype, evaluation rubric, MCP prototype, cost validation).
