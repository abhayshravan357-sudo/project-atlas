# Problem Definition — Project Atlas

## What specific problem does Atlas address?

Before building a software project, teams face several research and decision challenges:

1. **Technology selection without evidence.** Teams pick frameworks, languages, and libraries based on familiarity or popularity rather than a structured comparison of fit, cost, security, and maintenance implications.

2. **Architecture commitment too early.** A single architecture is chosen without evaluating alternatives (orchestrator-worker, sequential pipeline, hierarchical, peer-to-peer, etc.) against the project's actual constraints.

3. **No organized research base.** Findings from research are scattered across chats, notes, and individual memories, with no central, version-controlled knowledge base that the whole team can reference.

4. **No clear decision trail.** Architectural and technology decisions are made without recorded reasoning, alternatives considered, or supporting evidence, making them hard to revisit or defend later.

5. **Research siloed in one person.** One individual often does all the research, creating a single point of failure and limiting breadth of exploration.

## Why is existing tooling insufficient?

Existing tools address parts of the problem but not the whole:
- **LLM chat interfaces** produce unstructured, non-versioned, non-synthesized output.
- **Research management tools** (Notion, wikis) store notes but do not coordinate parallel research or enforce evidence standards.
- **Agent frameworks** (LangGraph, AutoGen, ADK) orchestrate agents but do not provide the research-cycle management, Git-worktree isolation, or documentation standards Atlas requires.

## Pain points

- Decisions reversed later because alternatives were not considered
- Duplicate research across team members
- No single source of truth for why a technology was chosen
- New team members cannot reconstruct the reasoning behind the stack
