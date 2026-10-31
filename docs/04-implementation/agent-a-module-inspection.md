# Agent A Module Inspection — Atlas Orchestrator

## 1. Module name and file path

- **Module name:** `atlas.orchestrator` (class `Orchestrator`)
- **Source file:** `/home/abhaysawant/Downloads/expermint/atlast/src/atlas/orchestrator.py`
- **Inspected from worktree branch:** `agent-test-a` at `/home/abhaysawant/Downloads/expermint/project-atlas-worktrees/agent-test-a`
- **Inspection performed by:** Worker A (read-only; no changes made to the module)

## 2. What the module does (plain-language summary)

The orchestrator drives one complete Atlas research cycle. Given an objective and a list of research domains, it:

1. Plans the cycle by recording the domains.
2. Delegates by creating a dedicated Git branch and isolated worktree per domain.
3. Investigates by writing a placeholder research report into each worktree (a stand-in for real agent research).
4. Reports by collecting those reports.
5. Synthesizes the reports into a single synthesis document stored in the knowledge base.
6. Reviews by printing a review gate and marking the state as pending manager review.
7. Commits (via `commit_approved`, called only by the Manager Agent after approval) by merging each domain branch into `main` and removing its worktree.
8. Reassesses by setting the final phase to `reassess`.

It is intentionally dependency-free (Python standard library only) so it can run immediately. A future version may replace the hand-rolled state machine with LangGraph for checkpoints and human-in-the-loop interrupts.

## 3. Key classes/functions and their responsibilities

### Class `Orchestrator`

Manages one Atlas research cycle. Constructed with `repo_root`, `worktree_parent`, and `knowledge_base` paths; holds a `WorktreeManager` instance.

| Method | Responsibility |
|---|---|
| `__init__(repo_root, worktree_parent, knowledge_base)` | Resolves paths and instantiates the `WorktreeManager`. |
| `run_cycle(objective, domains)` | Public entry point. Creates `ResearchState`, runs all phases in order (`plan`, `delegate`, `investigate`, `report`, `synthesize`, `review`), then sets phase to `reassess` and returns the final state. |
| `_plan(state)` | Validates that domains are non-empty, logs the plan, advances phase to `delegate`. |
| `_delegate(state)` | For each domain, creates branch `research/<domain>` from `main` (if absent) via `WorktreeManager`, creates a worktree, records the path in `state.worktrees`, advances phase to `investigate`. |
| `_investigate(state)` | Placeholder: writes a `REPORT.md` into `docs/research/<domain>/` of each worktree, records report paths, advances phase to `report`. |
| `_report(state)` | Collects reports (already stored during investigate), logs count, advances phase to `review`. |
| `_synthesize(state)` | Combines all reports into `knowledge_base/cycle-synthesis.md`, records the path, advances phase to `commit`. |
| `_review(state)` | Human-in-the-loop review gate: sets `review_status = "pending"`, prints the state summary and instructions for the Manager Agent, advances phase to `review`. |
| `commit_approved(state)` | Manager-only merge step. Requires `review_status == "approved"`; merges each `research/<domain>` branch into `main` (no-ff), removes each worktree, advances phase to `reassess`. |

### Collaborating classes (referenced, not defined here)

- `ResearchState` (`atlas/state.py`): mutable dataclass carrying objective, domains, worktrees, reports, synthesis, review_status, current_phase, and message log.
- `WorktreeManager` (`atlas/worktree_manager.py`): Git worktree/branch operations (subprocess-backed `git` CLI wrapper).

## 4. How it fits into the Atlas research cycle

`orchestrator.py` is the cycle engine itself. Its phase sequence maps directly onto the Atlas research cycle:

`plan` → `_plan`
`delegate` → `_delegate`
`investigate` → `_investigate`
`report` → `_report`
`synthesize` → `_synthesize`
`review` → `_review`
`commit` → `commit_approved` (Manager Agent gated)
`reassess` → set at end of `run_cycle` and after `commit_approved`

The review/commit boundary is the manager handoff: `run_cycle` pauses at `_review` (pending review), and `commit_approved` must be invoked separately by the Manager Agent once `review_status` is set to `approved`.

## 5. Dependencies (imports, external packages)

Only Python standard library:

- `from __future__ import annotations`
- `from pathlib import Path`
- `from typing import Optional`
- `from .state import ResearchState`
- `from .worktree_manager import WorktreeManager`

No external packages (no LangGraph yet). `WorktreeManager` shells out to the `git` CLI via `subprocess`, so a Git installation is an implicit runtime requirement.

## 6. Limitations and observations

- **Placeholder investigation:** `_investigate` writes a templated placeholder report, not real research. Actual agent research must be wired in before this is production-usable.
- **Manual review gate:** `_review` only prints instructions and sets `review_status = "pending"`; it does not block or enforce a decision. The Manager Agent must manually set `review_status` before `commit_approved` can proceed.
- **Branch source fixed to `main`:** `_delegate` always branches from `main` ("the approved base"), which is correct for isolation but means the orchestrator must run against a repo with a `main` branch.
- **Worktree collision:** `create_worktree` raises `FileExistsError` if a worktree directory already exists; re-running a cycle for the same domain without cleanup will fail.
- **Private API use in commit:** `commit_approved` calls `self.worktree_manager._run(...)` directly, reaching into a private helper.
- **No error recovery:** A phase failure aborts `run_cycle` with no checkpoint/resume; the docstring notes a future LangGraph migration for checkpoints and interrupts.
- **Single cycle per run:** `run_cycle` executes one objective; there is no built-in loop across multiple cycles (reassess is a terminal phase marker, not an automatic restart).

WORKER_A_COMPLETE: yes
File created: /home/abhaysawant/Downloads/expermint/project-atlas-worktrees/agent-test-a/docs/04-implementation/agent-a-module-inspection.md
