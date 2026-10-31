# Agent Registry — Project Atlas

Agent identities, responsibilities, branch names, and assignment statuses.

## Agents

| ID | Name | Role | Branch | Worktree | Assignment | Status |
|----|------|------|--------|----------|------------|--------|
| A | Agent A | Fundamentals Investigator | research/fundamentals | /tmp/atlast-wt/fundamentals | Cycle 1: fundamentals | complete |
| B | Agent B | Technology Researcher | research/technology-landscape | /tmp/atlast-wt/technology-landscape | Cycle 1: technology landscape | complete |
| C | Agent C | Architecture Researcher | research/architecture | /tmp/atlast-wt/architecture | Cycle 1: system architecture | complete |
| D | Agent D | Real-World Applications Researcher | research/real-world-applications | /tmp/atlast-wt/real-world-applications | Cycle 1: real-world applications | complete |
| E | Agent E | Academic Researcher | research/academic-literature | /tmp/atlast-wt/academic-literature | Cycle 1: academic literature | complete |
| F | Agent F | Innovation Explorer | research/innovation | /tmp/atlast-wt/innovation | Cycle 1: innovation exploration | complete |
| G | Agent G | Critical Analyst | research/critical-analysis | /tmp/atlast-wt/critical-analysis | Cycle 1: critical analysis | complete |

## Agent Responsibilities (Standard)

- Investigate assigned domain independently.
- Produce a research report in `docs/research/<domain>/`.
- Cite credible sources with links and dates where available.
- Distinguish FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL.
- Report completion; do NOT commit, merge, or push.

## Execution Note

Subagent (`task`) spawning is unavailable in this environment. The Main Agent is executing research assignments directly as branch manager, using the per-domain ASSIGNMENT.md prompts created in each worktree. Agents do NOT commit, merge, or push; the Main Agent reviews and commits approved work.

## Main Agent Responsibilities

- Review each report for accuracy, completeness, source quality.
- Assign status: APPROVED / REVISION REQUIRED / EXPAND / REJECTED.
- Stage and commit approved changes on the corresponding branch.
- Merge approved branches into main.
- Update this registry and all management docs.
