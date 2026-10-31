# API Design — Project Atlas

## Overview

Project Atlas is currently a documentation and research-orchestration system, not a networked application with external API consumers. The "API" in this context refers to the internal interfaces between orchestrator nodes, workers, and MCP tool servers.

## Internal interfaces

### Orchestrator node interface

Each LangGraph node follows this signature:

```python
def node_name(state: ResearchState) -> ResearchState:
    ...
```

- **Input**: Shared `ResearchState` (objective, domains, worktrees, reports, synthesis, review_status, current_phase).
- **Output**: Updated `ResearchState` with changes relevant to the node.

### MCP tool interface

MCP servers expose tools via a standardized client-server model:

| Method | Purpose |
|--------|---------|
| tools/list | Discover available tools on a server |
| tools/call | Invoke a tool with arguments |

### Worker assignment interface

Each worker receives an assignment prompt containing:
- Agent identity and specialization
- Git branch and worktree path
- Research objective and questions
- Required output files
- Restrictions and completion criteria

## External API considerations

Atlas does not expose a public HTTP API in the initial scope. Future considerations (not in scope):
- REST API for submitting research objectives
- WebSocket for real-time agent status
- MCP server for programmatic agent tool access

## Status

Proposed — no API implementation exists yet.
