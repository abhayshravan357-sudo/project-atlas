# Project Atlas Research Documentation

This directory contains the research knowledge base for Project Atlas, a multi-agent research and exploration orchestrator.

## Structure

| Directory | Purpose |
|-----------|---------|
| `management/` | Project operation tracking (progress, task board, agent registry, decision log, roadmap) |
| `research/` | Individual agent research reports by domain |
| `knowledge-base/` | Synthesized concepts, technologies, architecture patterns, use cases, papers |
| `comparisons/` | Technology, architecture, and approach comparison matrices |
| `experiments/` | Proposed experiments, feasibility studies, validation plans |
| `strategy/` | Project directions, opportunities, recommendations, decision records |
| `reports/` | Agent reports, synthesis, progress tracking |

## Workflow

This phase is research-and-exploration-first. No application code is created unless explicitly authorized.

1. Management establishes research domains and assigns agents.
2. Agents investigate independent domains on dedicated Git branches.
3. The Main Agent reviews each report (APPROVED / REVISION REQUIRED / EXPAND / REJECTED).
4. Approved findings are synthesized into `knowledge-base/` and `comparisons/`.
5. Approved branches are merged into `main` by the Main Agent.

## Status Legend

- **FACT**: Supported by credible evidence with a source link.
- **INTERPRETATION**: A conclusion derived from evidence.
- **HYPOTHESIS**: An idea requiring validation.
- **PROPOSAL**: A suggested direction for Project Atlas.
