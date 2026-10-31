# Test Cases — Project Atlas

## Existing test cases

| ID | Test | What it verifies | Location |
|----|------|------------------|----------|
| TC-01 | test_state_summary_contains_objective | ResearchState.summary() includes objective and domains | tests/test_orchestrator.py |
| TC-02 | test_worktree_manager_uses_provided_paths | WorktreeManager stores repo_root and worktree_parent correctly | tests/test_orchestrator.py |
| TC-03 | test_state_defaults | ResearchState has correct default values | tests/test_orchestrator.py |
| TC-04 | test_run_cycle_prints_summary | CLI run-cycle produces expected output with objective and domain | tests/test_cli.py |
| TC-05 | test_status_runs | CLI status command executes without error | tests/test_cli.py |
| TC-06 | test_review_approve | CLI review approve command records decision | tests/test_cli.py |

## Planned test cases (future milestones)

| ID | Test | What it verifies | Priority |
|----|------|------------------|----------|
| TC-07 | test_delegate_creates_worktree | Delegate phase creates branch + worktree per domain | High |
| TC-08 | test_synthesize_writes_kb | Synthesize phase writes knowledge-base file | High |
| TC-09 | test_commit_approved_merges | Commit phase merges approved branch into main | High |
| TC-10 | test_cli_commit_rejects_unapproved | CLI commit fails when review_status is not approved | Medium |
| TC-11 | test_mcp_filesystem_server | MCP filesystem server respects worktree sandbox | Medium |

## Test naming convention

Tests are named `test_<description>` and placed in `tests/test_<module>.py`, mirroring the source module under `src/atlas/`.
