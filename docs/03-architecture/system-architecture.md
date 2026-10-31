# System Architecture — Project Atlas

## Overview

Project Atlas is a multi-agent research and exploration orchestrator. Its core responsibility is to coordinate independent research agents across multiple domains, synthesize their findings into a centralized knowledge base, and guide incremental implementation of the project it helps design.

## Architectural pattern

Atlas uses the **orchestrator-worker pattern** with **git-worktree agent isolation**:

- A lead agent (orchestrator / Manager Agent) decomposes a research objective into independent domains.
- Each domain is assigned to a worker agent operating in an isolated Git worktree on its own branch.
- Workers produce research reports; the orchestrator synthesizes approved reports into the knowledge base.
- All integration (commits, merges) is performed by the Manager Agent on `main`.

## High-level architecture (Mermaid)

```mermaid
graph TD
    Owner[Project Owner] --> Main[Manager Agent / Orchestrator<br/>main branch]
    
    Main --> Plan[PLAN: define objectives & questions]
    Plan --> Delegate[DELEGATE: create branch + worktree per domain]
    
    Delegate --> W1[Worker: Documentation<br/>worktree: docs-foundation]
    Delegate --> W2[Worker: Technology<br/>worktree: tech-stack]
    Delegate --> W3[Worker: Architecture<br/>worktree: arch-system]
    
    W1 --> R1[(Research Report)]
    W2 --> R2[(Research Report)]
    W3 --> R3[(Research Report)]
    
    R1 --> Review[REVIEW: approve / revise / reject]
    R2 --> Review
    R3 --> Review
    
    Review --> Synth[SYNTHESIZE: knowledge base]
    Synth --> Commit[COMMIT: merge to main]
    Commit --> Reassess[REASSESS: next cycle]
    Reassess --> Main
    
    KB[docs/knowledge-base/]:::store
    Synth --> KB
    
    classDef store fill:#e1f5e1,stroke:#2e7d32;
    class KB store;
    
    style Main fill:#f3e5f5,stroke:#7b1fa2
    style Review fill:#fff3e0,stroke:#e65100
    style Commit fill:#e8f5e9,stroke:#2e7d32
```

## System boundaries

**In scope:**
- Research orchestration (plan → delegate → investigate → report → review → synthesize → commit → reassess)
- Git-worktree agent isolation
- Research report generation with evidence classification (FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL)
- Knowledge base synthesis
- Technology and architecture comparison documentation
- Evaluation rubric (LLM-as-judge + human review)
- Management documentation (dashboard, task register, decisions, changelog)

**Out of scope:**
- General-purpose LLM chatbot
- Web search engine or crawler
- Autonomous code generation for arbitrary applications
- Deployment/DevOps platform
- User authentication or multi-tenancy

## Component responsibilities

| Component | Responsibility |
|-----------|---------------|
| Manager Agent (Orchestrator) | Coordinates cycles, creates branches/worktrees, assigns tasks, reviews deliverables, commits/merges to main |
| Worker Agents | Execute assigned research/implementation in isolated worktrees, produce deliverables |
| Git worktrees | Filesystem isolation per domain; each on its own branch |
| Knowledge base (docs/knowledge-base/) | Synthesized findings from approved reports |
| Management docs (docs/09-management/) | Dashboard, task register, decisions, changelog, roadmap |
| Source code (src/) | Application implementation (planned, not yet built) |
| Tests (tests/) | Test suite (planned, not yet built) |

## Data flow

1. Owner submits a research objective to the Manager Agent.
2. Manager decomposes the objective into independent domains.
3. Manager creates a Git branch and worktree per domain.
4. Workers execute research in isolation, producing reports.
5. Manager reviews each report (APPROVED / REVISION REQUIRED / REJECTED).
6. Approved reports are synthesized into docs/knowledge-base/.
7. Manager merges approved branches into main.
8. Cycle reassesses and plans the next investigation.
