# Testing Strategy — Project Atlas

## Overview

Project Atlas follows a documentation-first, test-backed development approach. Every implementation milestone is accompanied by tests, and documentation is kept in sync with code changes.

## Test pyramid

| Level | Purpose | Tools | Location |
|-------|---------|-------|----------|
| Unit | Test individual functions/classes in isolation | pytest | tests/ |
| Integration | Test component interactions (orchestrator + worktree manager) | pytest | tests/ |
| CLI | Test command-line interface behavior | click.testing.CliRunner | tests/ |
| Documentation | Verify docs exist and are current | Manual review + CI check | docs/ |

## Testing principles

1. **Every feature has a test.** No implementation milestone is considered complete without at least one test case.
2. **Tests are fast and dependency-free.** The core orchestrator uses only the Python standard library so tests run without installing external packages.
3. **Tests are deterministic.** No reliance on network, LLM APIs, or external services.
4. **Documentation is part of the deliverable.** Every code change includes a documentation update.

## What is tested

| Area | What | Where |
|------|------|-------|
| Research state | ResearchState defaults, summary, logging | tests/test_orchestrator.py |
| Worktree manager | Path handling, branch/worktree creation logic | tests/test_orchestrator.py |
| CLI | run-cycle, status, review commands | tests/test_cli.py |

## What is NOT yet tested (future)

- LLM provider integration (requires API keys, out of scope for unit tests)
- MCP server behavior (requires MCP implementations)
- End-to-end research cycle with real worker agents
- Git merge conflict resolution

## Test execution

```bash
# From the Atlas repository root
pytest
```

## Coverage goal

Aim for high coverage of the orchestrator and CLI. As new components are added (MCP servers, LangGraph migration), add corresponding tests before considering the feature complete.

## Test-driven workflow

For every feature:
1. Write the requirement (docs/01-requirements/).
2. Write the test.
3. Implement the feature.
4. Run tests (must pass).
5. Update documentation.
6. Commit and merge.
