# Phase 6.1 — Git Integration Testing

## What was added

| File | Purpose |
|------|---------|
| `tests/test_git_integration.py` | Integration tests against real temporary Git repositories and worktrees |

## Why it was needed

The existing unit tests verified `WorktreeManager` path handling but never touched a real Git repository. Phase 6.1 requires integration tests that create actual temporary Git repos and worktrees to prove branch creation, worktree isolation, existing-worktree detection, cleanup, and main-worktree protection.

## Technology / package involved

- **Git CLI** (`git init`, `git worktree add`, `git branch`, `git checkout`) — exercised via `subprocess`
- **tempfile** — throwaway repositories and worktree parents
- **pytest** — test runner

## Where it exists in the repository

- `tests/test_git_integration.py` — all integration tests

## How it works

Each test creates a fresh temporary Git repository initialized on `main`, plus a separate worktree parent directory. No production repository or worktree is touched.

Tests cover:

| Test | What it verifies |
|------|-----------------|
| `test_worktree_manager_uses_provided_paths` | Manager is constructed with correct repo/worktree paths |
| `test_create_branch_and_worktree` | `create_worktree` creates a branch + worktree on that branch |
| `test_branch_created_from_main_not_current` | Branches are created from `main`, not the currently checked-out branch |
| `test_worktrees_are_isolated` | Files written in one worktree are invisible in another |
| `test_list_worktrees_returns_created_paths` | `list_worktrees` returns all registered worktree paths |
| `test_create_worktree_rejects_existing` | Creating a duplicate worktree raises `FileExistsError` |
| `test_remove_worktree` | `remove_worktree` deletes a clean worktree |
| `test_remove_worktree_with_force` | `remove_worktree(force=True)` deletes a dirty worktree |
| `test_invalid_repository_raises` | A non-git directory raises an error |
| `test_orchestrator_delegate_creates_worktrees` | Orchestrator `run_cycle` creates worktrees + placeholder reports per domain |
| `test_cleanup_after_failure` | Force-removal cleans up after a "failed" cycle |
| `test_main_worktree_not_removed` | Worktree operations never touch the main checkout |

## How to run and test it

```bash
# From the project root
python -m pytest tests/test_git_integration.py -v
```

All tests use `tempfile.TemporaryDirectory`, so nothing persists after the test run.

## What the owner should learn

- Worktree creation always branches from `main`, keeping the approved baseline clean.
- Each domain's worktree is isolated; agents cannot read or write each other's files.
- Duplicate worktrees and dirty worktrees are handled safely (error / force-remove).
- Invalid (non-git) repositories fail loudly instead of silently corrupting state.
- The main worktree is never modified or removed by worktree operations.

## Limitations and alternatives

- **Limitation:** These tests shell out to the `git` CLI, so they require Git to be installed (it is, in this environment).
- **Alternative:** Use a Python Git library like `gitpython`, but that adds a dependency the project currently avoids.
- **Limitation:** Tests run serially; parallel test execution with shared temp dirs could collide. `tempfile.mkdtemp` mitigates this.
