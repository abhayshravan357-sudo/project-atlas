# Agent I Report — Cycle 2 Technology Comparison

## Technology Comparison Matrix

| Framework | Core orchestration model | State / persistence | Human-in-the-loop | Git-worktree fit | Token cost | Complexity | Lock-in risk | Atlas suitability |
|-----------|-------------------------|---------------------|-------------------|------------------|------------|------------|--------------|-------------------|
| LangGraph | Graph-based (nodes=agents, edges=control flow; supports cycles) | Checkpoints / persistence built-in | Interrupts & breakpoints | Low (in-process Python) | Medium-High | High | Medium (LangChain ecosystem) | High |
| Google ADK | Sequential / coordinator-dispatcher / hierarchical | session.state via output_key | Not native | Low (in-process Python) | Medium | Medium | Medium (Google ecosystem) | High |
| AutoGen / Microsoft Agent Framework | Conversation-driven message passing | Conversation history | Limited | Low (in-process .NET/Python) | Medium-High | Medium-High | High (Microsoft ecosystem) | Medium-High |

## Individual Framework Profiles

### LangGraph
**Core model:** Graph-based orchestration. Agents are nodes; edges define control flow including cycles (loops) and conditional routing. Compiles a StateGraph into a runnable.
**State/persistence:** Checkpoints persist state across steps; supports time-travel debugging and human-in-the-loop interrupts.
**Human-in-the-loop:** Native interrupt/breakpoint mechanism for review at any graph node.
**Git-worktree fit:** Low. Designed for in-process Python agents sharing memory, not isolated filesystem worktrees. Requires custom glue.
**Token cost:** Medium-High. Graph execution with multiple nodes and checkpoints increases token usage.
**Complexity:** High. Steep learning curve; Python-centric.
**Lock-in risk:** Medium. LangChain ecosystem; concepts portable but implementation tied to LangChain.
**Atlas suitability:** High. Graph model maps naturally to the research cycle (plan→delegate→...→reassess with loops).

### Google ADK
**Core model:** Agent Development Kit with three orchestration patterns: sequential (pipeline), coordinator/dispatcher (concierge), and hierarchical (top-down delegation).
**State/persistence:** session.state with output_key lets the next agent pick up where the prior left off.
**Human-in-the-loop:** Not a native core feature; must be layered on.
**Git-worktree fit:** Low. In-process Python agents; not filesystem-isolated.
**Token cost:** Medium. Depends on pattern; sequential is cheaper than parallel.
**Complexity:** Medium. Cleaner API than LangGraph; Google model ecosystem.
**Lock-in risk:** Medium. Google models and Cloud IAM.
**Atlas suitability:** High. State management and pattern variety fit the cycle model; coordinator/dispatcher fits the manager role.

### AutoGen / Microsoft Agent Framework
**Core model:** Conversation-driven multi-agent orchestration. Agents converse via messages; code-driven coordination and tool use. Merged with Semantic Kernel (Oct 2025) for enterprise features.
**State/persistence:** Conversation history serves as state.
**Human-in-the-loop:** Limited native support; human can be added as a participant agent.
**Git-worktree fit:** Low. In-process agents; not filesystem-isolated.
**Token cost:** Medium-High. Conversation-based coordination can generate many turns.
**Complexity:** Medium-High. Ecosystem convergence in progress (AutoGen + Semantic Kernel).
**Lock-in risk:** High. Microsoft ecosystem; .NET/Python.
**Atlas suitability:** Medium-High. Proven conversation model; enterprise backing; but convergence adds uncertainty.

## Recommendation

**Primary candidate: LangGraph.** Its graph model with cycles, persistence, and native human-in-the-loop interrupts maps most directly to Atlas's research cycle. The main drawback is the git-worktree fit, which requires custom glue regardless of framework choice.

**Secondary candidate: Google ADK.** Strong state management (session.state) and the coordinator/dispatcher pattern fit the manager role. Good fallback if LangGraph's complexity is prohibitive.

**Not recommended for cycle 2:** AutoGen, due to ecosystem convergence uncertainty and higher lock-in risk.

## Open Questions

- How much custom glue is needed to connect any framework to git-worktree isolation?
- Is the human-in-the-loop interrupt sufficient for the manager review gate, or is a separate review process needed?
- Can framework state (checkpoints/session.state) be persisted across separate worktree executions?

## Sources
- LangChain / LangGraph documentation — https://langchain.com (2026)
- Google ADK developer's guide — https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk, 2025-12-16
- AutoGen / Microsoft Agent Framework — Microsoft blog, "Designing Multi-Agent Intelligence", 2025-08-20 — https://developer.microsoft.com/blog/designing-multi-agent-intelligence/
- MDPI Systems survey, Zhu et al., 2026-06-01 — https://www.mdpi.com/1999-5903/18/6/326
