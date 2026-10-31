# Component Architecture — Project Atlas

## Component diagram (Mermaid)

```mermaid
graph TD
    subgraph Management[Management Layer]
        Dashboard[Agent Dashboard]
        TaskRegister[Task Register]
        Decisions[Decisions Log]
        Changelog[Changelog]
        Roadmap[Development Roadmap]
    end
    
    subgraph Orchestration[Orchestration Layer]
        Manager[Manager Agent / Orchestrator]
        Plan[Plan Node]
        Delegate[Delegate Node]
        Synthesize[Synthesize Node]
        Review[Review Gate]
        Commit[Commit/Merge Node]
    end
    
    subgraph Workers[Worker Layer]
        W1[Worker: Documentation]
        W2[Worker: Technology]
        W3[Worker: Architecture]
        W4[Worker: Implementation]
        W5[Worker: QA/Testing]
    end
    
    subgraph Isolation[Isolation Layer]
        WT1[Git Worktree: docs-foundation]
        WT2[Git Worktree: tech-stack]
        WT3[Git Worktree: arch-system]
        WT4[Git Worktree: impl-core]
        WT5[Git Worktree: test-qa]
    end
    
    subgraph Knowledge[Knowledge Base]
        KB[docs/knowledge-base/]
        Comparisons[docs/comparisons/]
        Experiments[docs/experiments/]
    end
    
    Manager --> Plan
    Plan --> Delegate
    Delegate --> WT1
    Delegate --> WT2
    Delegate --> WT3
    WT1 --> W1
    WT2 --> W2
    WT3 --> W3
    W1 --> R1[(Report)]
    W2 --> R2[(Report)]
    W3 --> R3[(Report)]
    R1 --> Review
    R2 --> Review
    R3 --> Review
    Review --> Synthesize
    Synthesize --> KB
    Review --> Commit
    Commit --> Main[main branch]
    
    Manager --> Dashboard
    Manager --> TaskRegister
    Manager --> Decisions
    Manager --> Changelog
    Manager --> Roadmap
    
    style Manager fill:#f3e5f5,stroke:#7b1fa2
    style Review fill:#fff3e0,stroke:#e65100
    style Commit fill:#e8f5e9,stroke:#2e7d32
```

## Component responsibilities

| Component | Responsibility | Inputs | Outputs |
|-----------|---------------|--------|---------|
| Manager Agent | Orchestrates the research cycle; creates branches/worktrees; reviews deliverables; commits/merges | Research objective; worker reports | Branches; worktrees; merged main; knowledge base |
| Plan Node | Decomposes objective into independent domains | Objective | Domain list |
| Delegate Node | Creates branch + worktree per domain | Domain list | Branch names; worktree paths |
| Worker | Executes assigned task in isolated worktree | Assignment prompt | Deliverable (report/code) |
| Review Gate | Human-in-the-loop: APPROVED / REVISION REQUIRED / REJECTED | Worker deliverable | Decision |
| Synthesize Node | Combines approved reports into knowledge base | Approved reports | docs/knowledge-base/ entries |
| Commit/Merge Node | Merges approved branches into main | Approved branch | Updated main |
| Git worktree | Isolated working directory per domain | Branch | Working files |
| Knowledge base | Centralized synthesized findings | Approved reports | Structured documentation |

## Inter-component communication

- **Manager ↔ Workers**: Through assignment prompts and worktrees (no direct process communication; workers operate independently).
- **Workers → Manager**: Through deliverable files placed in their worktrees.
- **Manager → Git**: Through commits and merges on branches/worktrees.
- **Manager → Knowledge base**: Through synthesized documentation files.

## Data ownership

- **Worktrees**: Owned by the worker assigned to that domain; no other worker may modify.
- **main branch**: Owned exclusively by the Manager Agent.
- **docs/**: Shared documentation; updated by workers in their domain and by the Manager during integration.
- **src/**: Application source code (planned); owned by implementation workers.
