# Agent Registry — Project Atlas

Agent identities, responsibilities, branch names, and assignment statuses.

## Agents

| ID | Name | Role | Branch | Worktree | Assignment | Status |
|----|------|------|--------|----------|------------|--------|
| A | Agent A | Fundamentals Investigator | research/fundamentals | — | Cycle 1: fundamentals | unassigned |
| B | Agent B | Technology Researcher | research/technology-landscape | — | Cycle 1: technology landscape | unassigned |
| C | Agent C | Architecture Researcher | research/architecture | — | Cycle 1: system architecture | unassigned |
| D | Agent D | Real-World Applications Researcher | research/real-world-applications | — | Cycle 1: real-world applications | unassigned |
| E | Agent E | Academic Researcher | research/academic-literature | — | Cycle 1: academic literature | unassigned |
| F | Agent F | Innovation Explorer | research/innovation | — | Cycle 1: innovation exploration | unassigned |
| G | Agent G | Critical Analyst | research/critical-analysis | — | Cycle 1: critical analysis | unassigned |

## Agent Responsibilities (Standard)

- Investigate assigned domain independently.
- Produce a research report in `docs/research/<domain>/`.
- Cite credible sources with links and dates where available.
- Distinguish FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL.
- Report completion; do NOT commit, merge, or push.

## Main Agent Responsibilities

- Review each report for accuracy, completeness, source quality.
- Assign status: APPROVED / REVISION REQUIRED / EXPAND / REJECTED.
- Stage and commit approved changes on the corresponding branch.
- Merge approved branches into main.
- Update this registry and all management docs.
