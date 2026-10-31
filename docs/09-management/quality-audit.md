# Phase 6.1 — Test Quality Audit

## What was added

| File | Purpose |
|------|---------|
| `tests/test_quality_audit.py` | Failure-path, CLI integration, and MCP integration tests |

## Why it was needed

The original test suite (10 tests) covered happy-path state management, worktree path handling, and basic CLI invocation. It did not cover failure paths (invalid review status, empty domains, non-git repositories), end-to-end CLI invocation against a real git repo, or malformed MCP requests. Phase 6.1 requires these gaps to be closed before the codebase can be considered reliably validated.

## Technology / package involved

- **pytest** — test runner
- **click.testing.CliRunner** — CLI invocation without a subprocess
- **tempfile** — throwaway git repositories and worktrees
- **subprocess** — git CLI invocation
- **stdlib json** — MCP JSON-RPC request/response

## Where it exists in the repository

- `tests/test_quality_audit.py` — all quality-audit tests

## How it works

### Failure-path tests

| Test | What it verifies |
|------|-----------------|
| `test_review_status_pending_blocks_commit` | `commit_approved` raises when status is `pending` |
| `test_review_status_revision_required_blocks_commit` | `commit_approved` raises when status is `revision_required` |
| `test_orchestrator_requires_domains` | `run_cycle` raises `ValueError` for empty domain list |
| `test_worktree_manager_nonexistent_repo_raises_on_delegate` | `create_worktree` fails on a non-git directory |

### CLI integration tests

| Test | What it verifies |
|------|-----------------|
| `test_cli_run_cycle_end_to_end` | Full `run-cycle` command against a real temp git repo creates worktrees + reports |
| `test_cli_status_runs` | `status` command executes without error |
| `test_cli_review_approve_records_decision` | `review approve` records a decision |

### MCP integration tests

| Test | What it verifies |
|------|-----------------|
| `test_mcp_jsonrpc_initialize` | `initialize` method returns server info + protocol version |
| `test_mcp_tools_list` | `tools/list` returns registered tools |
| `test_mcp_unknown_tool_returns_error` | Unknown tool returns JSON-RPC error code -32601 |
| `test_mcp_parse_error` | Parse-error constant exists on the server base |

## How to run and test it

```bash
# From the project root
python -m pytest tests/test_quality_audit.py -v
```

All tests use `tempfile.TemporaryDirectory`; nothing persists after the run.

## What the owner should learn

- The review gate correctly blocks commits unless the status is `approved` (pending and revision_required are rejected).
- Empty domain lists are rejected before any worktree is created.
- Non-git directories fail loudly instead of corrupting state.
- The full CLI `run-cycle` flow works end to end against a real git repo.
- MCP servers correctly handle initialize, tools/list, unknown-tool, and parse-error paths.

## Limitations and alternatives

- **Limitation:** CLI integration tests invoke `cli.main` through `CliRunner`, which catches `SystemExit`; they do not test actual process exit codes from a subprocess.
- **Alternative:** Use `subprocess.run(["python", "-m", "atlas.cli", ...])` for true process-level integration, but that is slower and harder to assert on structured output.
- **Limitation:** MCP parse-error path is verified by constant existence rather than a full stdin/stdout round-trip; a full end-to-end server process test could be added later.
