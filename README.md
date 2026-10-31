# Project Atlas — MCP Servers

This directory contains MCP (Model Context Protocol) servers that expose tools
to Atlas agents.  Servers use stdio JSON-RPC 2.0 and require no external
``mcp`` package (standard library only).

## Servers

| Server | Purpose | Tools |
|--------|---------|-------|
| ``filesystem_server.py`` | Read/write files, list directories | read_file, write_file, list_directory |
| ``git_server.py`` | Read-only git operations | git_branch, git_status, git_diff |

## Security model

- **Filesystem server** is scoped to a single root directory (the agent's assigned worktree). Attempts to read/write outside the root are rejected.
- **Git server** is read-only: agents can inspect branches, status, and diffs, but cannot commit or push. Commit remains the Manager Agent's responsibility.

## How to run

```bash
# Filesystem server (scoped to a worktree)
python -m atlas.mcp.filesystem_server /path/to/worktree

# Git server (scoped to a repo)
python -m atlas.mcp.git_server /path/to/repo
```

Each server reads JSON-RPC requests from stdin and writes responses to stdout.

## How to test

```bash
pytest
```

## Relationship to D-02/D-03

D-02 selected MCP for agent tool access. D-03 designed the system architecture with MCP servers as the tool layer. D-07 implements the first two servers (filesystem, git).

## Next steps

- Add an LLM provider server (llm_completion tool).
- Add a knowledge-base server (kb_search, kb_get).
- Wire servers into the orchestrator via an MCP client (LangGraph migration).
