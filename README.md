# Project Atlas — CLI Interface

This directory enhances the command-line interface for Project Atlas using
Click. It builds on the core orchestrator implemented in D-04.

## Commands

```bash
# Run a research cycle
python -m atlas.cli run-cycle "Compare LangGraph vs ADK" \
  --domains fundamentals,technology-landscape

# Show current state
python -m atlas.cli status

# Record a review decision
python -m atlas.cli review approve

# Commit approved branches into main
python -m atlas.cli commit
```

## How to run tests

```bash
pytest
```

## Relationship to D-04

D-04 created the core orchestrator (Orchestrator, ResearchState, WorktreeManager).
D-05 adds a Click-based CLI on top of it. The orchestrator logic is unchanged;
the CLI is a thin interface layer.

## Next steps

- Persist ResearchState to disk so review/commit decisions survive across CLI invocations.
- Wire the review gate into the orchestrator's LangGraph interrupt (future migration).
- Add more subcommands (worktree list, branch list, etc.).
