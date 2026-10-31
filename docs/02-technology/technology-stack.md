# Technology Stack — Project Atlas

## Stack overview

| Technology | Category | Version | Purpose | Status |
|------------|----------|---------|---------|--------|
| Python | Programming language | 3.10+ | Primary implementation language | Proposed |
| LangGraph | Orchestration framework | Latest | Agent orchestration (plan→delegate→investigate→report→review→synthesize→commit→reassess cycle) | Proposed |
| MCP | Integration protocol | Latest | Standardized agent-to-tool communication | Proposed |
| Git / git worktrees | Version control | Latest | Agent isolation, branch-per-domain, clean main | Implemented |
| pytest | Testing framework | Latest | Unit and integration tests | Proposed |
| Click / Typer | CLI framework | Latest | Command-line interface (future) | Optional |
| Mermaid | Diagramming | Latest | Architecture and workflow diagrams in docs | Implemented |

## How components fit together

- **Python** is the implementation language for all components.
- **LangGraph** orchestrates the research cycle as a StateGraph with nodes (plan, delegate, investigate, report, synthesize, review, commit) and edges defining control flow including cycles and human-in-the-loop interrupts.
- **MCP** servers expose tools (filesystem, git, search, knowledge base) to agents via a client-server model.
- **Git worktrees** provide filesystem isolation: each research domain works on its own branch in its own directory.
- **pytest** validates components.
- **Mermaid** diagrams document architecture and workflows in docs/.
