# Project Atlas — Core Orchestrator

This directory contains the initial implementation of the Atlas research-cycle
orchestrator.  It is a dependency-free Python package (standard library only)
that demonstrates the `plan -> delegate -> investigate -> report -> review ->
synthesize -> commit -> reassess` cycle.

## What this implements

- `src/atlas/orchestrator.py` — `Orchestrator` class driving the cycle.
- `src/atlas/state.py` — `ResearchState`, the shared cycle state.
- `src/atlas/worktree_manager.py` — Git worktree creation per domain.
- `src/atlas/cli.py` — minimal command-line entry point.
- `tests/test_orchestrator.py` — unit tests.

## What it does NOT do yet

- No LLM calls (no `anthropic`, `openai`, or other provider SDK).
- No LangGraph (planned upgrade — see `docs/02-technology/frameworks.md`).
- No MCP servers (planned — see `docs/02-technology/technology-stack.md`).
- No real worker agents (placeholder reports are generated).

## How to run

```bash
# From the Atlas repository root
python -m atlas.cli "Compare LangGraph vs ADK for agent orchestration" \
  --domains fundamentals,technology-landscape,architecture \
  --repo . \
  --worktree-parent ../project-atlas-worktrees \
  --knowledge-base docs/knowledge-base
```

## How to test

```bash
pytest
```

## Next steps

- Replace placeholder investigation with real worker research (D-05 CLI, D-07 MCP).
- Migrate the hand-rolled state machine to LangGraph for checkpoints and
  native human-in-the-loop interrupts.
- Add the review-gate interrupt so the Manager Agent can APPROVE / REVISE /
  REJECT before merging.
