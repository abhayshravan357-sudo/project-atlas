# Backend Architecture — Project Atlas

## Overview

The backend is the orchestrator layer that manages the research cycle. It is implemented in Python using LangGraph as the orchestration framework.

## Architecture diagram (Mermaid)

```mermaid
graph TD
    subgraph LangGraph[LangGraph StateGraph]
        Plan[plan node]
        Delegate[delegate node]
        Investigate[investigate node]
        Report[report node]
        Synthesize[synthesize node]
        Review[review gate / interrupt]
        Commit[commit node]
    end
    
    subgraph State[Shared State]
        Objective[research_objective]
        Domains[domains[]]
        Worktrees[worktrees[]]
        Reports[reports[]]
        Synthesis[synthesis]
        ReviewStatus[review_status]
    end
    
    subgraph Tools[MCP / Tool Layer]
        FS[Filesystem server]
        Git[Git server]
        Search[Web search server]
        LLM[LLM provider server]
        KB[Knowledge base server]
    end
    
    Plan --> Delegate
    Delegate --> Investigate
    Investigate --> Report
    Report --> Synthesize
    Synthesize --> Review
    Review -->|Approve| Commit
    Review -->|Revise| Investigate
    Review -->|Reject| End[End]
    
    Plan --> State
    Delegate --> State
    Investigate --> State
    Report --> State
    Synthesize --> State
    
    Investigate --> Tools
    Report --> Tools
    Synthesize --> Tools
    
    style Review fill:#fff3e0,stroke:#e65100
    style Commit fill:#e8f5e9,stroke:#2e7d32
```

## Backend components

| Component | Technology | Responsibility |
|-----------|------------|----------------|
| LangGraph StateGraph | Python + langgraph | Orchestrates the research cycle nodes and edges |
| Shared state | TypedDict / Pydantic model | Carries objective, domains, worktrees, reports, synthesis, review status |
| Plan node | Python function | Decomposes objective into independent domains |
| Delegate node | Python function | Creates Git branch + worktree per domain |
| Investigate node | Python function | Worker executes research in worktree |
| Report node | Python function | Collects worker reports |
| Synthesize node | Python function | Combines approved reports into knowledge base |
| Review gate | LangGraph interrupt | Human-in-the-loop: APPROVED / REVISE / REJECT |
| Commit node | Python function | Manager merges approved branch to main |
| MCP client | Python + MCP SDK | Calls MCP servers for tool access |
| MCP servers | Filesystem, Git, Search, LLM, KB | Expose tools to agents |

## State schema

```python
class ResearchState(TypedDict):
    objective: str
    domains: list[str]
    worktrees: dict[str, str]  # domain -> worktree path
    reports: dict[str, str]    # domain -> report content
    synthesis: str
    review_status: str         # pending / approved / revision_required / rejected
    current_phase: str
```

## Node responsibilities

- **plan**: Takes the objective, decomposes into domains, returns domain list.
- **delegate**: For each domain, creates a Git branch and worktree; records paths in state.
- **investigate**: Worker executes in worktree; produces report file.
- **report**: Reads report files from worktrees; collects into state.
- **synthesize**: Combines approved reports into docs/knowledge-base/ entries.
- **review**: LangGraph interrupt; presents synthesis to Manager for APPROVED / REVISE / REJECT.
- **commit**: Manager-approved; merges branch to main.

## Status

Proposed — no backend source code exists yet. Implementation planned for D-04 (Core Orchestrator).
