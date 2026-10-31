# Agent B Report — Technology Landscape

## Technology Comparison Matrix

| Technology | Category | What it does | Maturity | Key strengths | Key weaknesses | Relevance to Atlas | Source |
|------------|----------|--------------|----------|---------------|----------------|-------------------|--------|
| LangGraph | Orchestration framework | Graph-based agent orchestration with cycles, persistence, human-in-the-loop | Mature (LangChain ecosystem) | Fine-grained control, cycles, checkpoints, streaming | Steep learning curve, Python-centric | High — fits graph research cycles | LangChain docs, 2026 |
| LangChain | Orchestration framework | LLM application framework, chains, agents, tool use | Mature | Broad integrations, large community | Legacy complexity, newer patterns superseded by LangGraph | Medium — foundational | LangChain docs, 2026 |
| CrewAI | Orchestration framework | Role-based agents, sequential/process workflows | Maturing | Simple role/task model, quick setup | Less flexible for complex graphs | Medium | CrewAI docs, 2026 |
| AutoGen / Microsoft Agent Framework | Orchestration framework | Conversation-driven multi-agent; merged with Semantic Kernel (Oct 2025) | Maturing | Conversation as coordination, enterprise features | Microsoft ecosystem, convergence in progress | High | MDPI survey, 2026-06-01; Microsoft blog, 2025-08-20 |
| Google ADK | Orchestration framework | Agent Development Kit; sequential, coordinator/dispatcher, hierarchical patterns | Maturing | State management (session.state), tool integration, Google model ecosystem | Google-centric | High | Google ADK guide, 2025-12-16 |
| OpenAI Swarm | Orchestration framework | Lightweight multi-agent orchestration (routine handoffs) | Experimental | Minimal, routine-oriented | Limited features, OpenAI-only | Low-Medium | OpenAI docs |
| OpenAI Agents SDK | Orchestration framework | Agent orchestration with built-in tools, tracing | Maturing | Tracing, built-in tools, OpenAI-native | OpenAI ecosystem | Medium | OpenAI docs |
| Model Context Protocol (MCP) | Integration standard | Standard for connecting LLMs to data/tools/servers | Emerging | Open standard, growing server ecosystem | Early, fragmentation risk | High — tool/context integration | mcp.so, 2025-2026 |
| Agent-to-Agent (A2A) | Integration protocol | Inter-agent communication protocol | Emerging | Standardized agent-to-agent messaging | Very early, limited adoption | Medium-High | Google/A2A, 2025-2026 |
| git / git worktrees | Version control | Distributed version control; isolated parallel working trees | Mature | Ubiquitous, reliable, branching/isolation | CLI complexity for non-technical users | High — Atlas isolation model | git-scm.com |
| Click / Typer | CLI framework | Python CLI building | Mature | Easy command definition, good UX | Python-only | Medium | Click/Typer docs |
| Vector DB (e.g., pgvector, Chroma, Qdrant) | Data | Store/query embeddings for knowledge retrieval | Maturing | Semantic search over knowledge base | Additional infra, embedding model choice | Medium | Vendor docs |

## Individual Technology Profiles

### LangGraph
**What it does:** Graph-based orchestration where agents are nodes and edges define control flow, including cycles (loops) and conditional routing. Supports persistence (checkpoints) and human-in-the-loop interrupts.
**How it works:** Define a StateGraph with nodes (agent functions) and edges; compile into a runnable; LangGraph manages state passing and persistence.
**Why it matters:** Fits Atlas's research cycle (plan→delegate→...→reassess) as a graph with possible loops back to earlier phases.
**Where used:** LangChain agents, production agent workflows.
**Advantages:** Fine-grained control, cycles, checkpoints, streaming, human-in-the-loop.
**Disadvantages:** Steep learning curve; Python-centric; operational complexity.
**Requirements:** Python, LangChain/LangGraph install, LLM provider.
**Dependencies:** LangChain ecosystem, LLM API.
**Complexity:** Medium-High.
**Cost:** Framework free; LLM token cost dominates.
**Security:** Standard LLM/app security; prompt injection via tool outputs.
**Alternatives:** LangChain, CrewAI, AutoGen, ADK.
**Relevance to Atlas:** High — graph model maps naturally to research cycle.

### LangChain
**What it does:** Broad LLM application framework with chains, agents, retrievers, memory, tool use.
**How it works:** Compose components (prompt, model, parser, tools) into chains/agents.
**Why it matters:** Foundational; largest integration ecosystem.
**Where used:** Most LLM applications.
**Advantages:** Huge integration library, large community, mature.
**Disadvantages:** Legacy abstraction complexity; newer orchestration better in LangGraph.
**Requirements:** Python/JS, LLM API.
**Dependencies:** LLM provider.
**Complexity:** Medium.
**Cost:** Free; LLM token cost.
**Security:** Standard; tool-output prompt injection.
**Alternatives:** LangGraph (successor pattern), CrewAI, ADK.
**Relevance to Atlas:** Medium — foundational but superseded for orchestration by LangGraph.

### AutoGen / Microsoft Agent Framework
**What it does:** Conversation-driven multi-agent orchestration; merged with Semantic Kernel (Oct 2025) to combine agent patterns with enterprise features.
**How it works:** Agents converse via messages; code-driven coordination; tool use.
**Why it matters:** Proven conversation-as-coordination model; enterprise backing.
**Where used:** Microsoft research, enterprise agents.
**Advantages:** Conversation model, enterprise features via Semantic Kernel, Microsoft backing.
**Disadvantages:** Ecosystem convergence in progress; complexity.
**Requirements:** .NET/Python, LLM API.
**Dependencies:** Semantic Kernel, LLM provider.
**Complexity:** Medium-High.
**Cost:** Free; LLM token cost.
**Security:** Enterprise auth features via Semantic Kernel.
**Alternatives:** LangGraph, CrewAI, ADK.
**Relevance to Atlas:** High — validated conversation-based coordination.

### Google ADK
**What it does:** Agent Development Kit with orchestration patterns (sequential, coordinator/dispatcher, hierarchical) and session state.
**How it works:** Define agents with tools; use SequentialAgent or coordinator delegation; state via output_key/session.state.
**Why it matters:** Google model ecosystem, clean state management, multiple patterns.
**Where used:** Google agent applications.
**Advantages:** State management, pattern variety, Google models.
**Disadvantages:** Google-centric; maturing.
**Requirements:** Python, Google Cloud/LLM API.
**Dependencies:** Google models.
**Complexity:** Medium.
**Cost:** Free; LLM token cost.
**Security:** Google Cloud IAM.
**Alternatives:** LangGraph, AutoGen, CrewAI.
**Relevance to Atlas:** High — state and delegation patterns fit cycle model.

### Model Context Protocol (MCP)
**What it does:** Open standard for connecting LLMs to data sources, tools, and servers via a client-server model.
**How it works:** MCP clients (hosts) connect to MCP servers exposing resources/tools/prompts over stdx/HTTP.
**Why it matters:** Standardizes tool/context integration; Atlas agents need tools.
**Where used:** Claude Desktop, growing server ecosystem.
**Advantages:** Open standard, decoupled servers, growing adoption.
**Disadvantages:** Early stage; server fragmentation; client support uneven.
**Requirements:** MCP client + servers; transport (stdio/HTTP).
**Dependencies:** LLM host with MCP support.
**Complexity:** Medium.
**Cost:** Free; hosting servers.
**Security:** Server authentication, tool permission models.
**Alternatives: Direct API integrations, A2A.
**Relevance to Atlas:** High — standardized tool access for agents.

### Agent-to-Agent (A2A)
**What it does:** Protocol for standardized inter-agent communication and task delegation.
**How it works:** Agents exchange structured messages/cards to delegate and report.
**Why it matters:** Enables interoperable multi-agent systems beyond one framework.
**Where used:** Early Google-led initiative.
**Advantages:** Standardized, framework-agnostic.
**Disadvantages:** Very early; limited implementations.
**Requirements:** A2A-compliant agents.
**Dependencies:** Protocol implementations.
**Complexity:** Medium-High.
**Cost:** Free.
**Security:** Message authentication, authorization.
**Alternatives:** Direct function calls, shared queues.
**Relevance to Atlas:** Medium-High — future inter-agent communication.

### git / git worktrees
**What it does:** Distributed version control; worktrees add isolated working directories per branch.
**How it works:** `git worktree add` checks out a branch into a separate directory sharing the object database.
**Why it matters:** Core to Atlas isolation model — one worktree per research domain, no file conflicts.
**Where used:** Software development.
**Advantages:** Ubiquitous, reliable, branching, isolation, cheap to create.
**Disadvantages:** CLI complexity; not designed for non-technical users.
**Requirements:** Git, filesystem.
**Dependencies:** None.
**Complexity:** Low-Medium.
**Cost:** Free.
**Security:** Standard repo security; secret leakage risk.
**Alternatives:** Multiple clones, container per agent.
**Relevance to Atlas:** High — the isolation mechanism itself.

## Languages Assessment

| Language | Ecosystem / LLM support | Concurrency | Deployment | Suitability for Atlas |
|----------|------------------------|-------------|------------|----------------------|
| Python | Best — dominant LLM/agent library support | GIL limits threads; async/process for parallelism | Easy (scripts, containers) | High — primary agent ecosystem |
| TypeScript/JS | Strong — growing agent/LLM libraries | Event loop, worker threads | Easy (Node, containers) | High — CLI/web frontends |
| Go | Moderate — fewer agent libraries | Excellent goroutines | Strong (static binaries) | Medium — good for orchestration runtime |
| Rust | Emerging — small agent library ecosystem | Excellent ownership/async | Strong | Low-Medium — immature agent ecosystem |

Python is the default choice for agent orchestration given library dominance; TypeScript is a strong secondary for CLI/tooling.

## Emerging Tech Watchlist
- MCP (tool/context standardization) — watch server ecosystem maturation.
- A2A (inter-agent protocol) — watch implementations.
- Local-first model execution (Ollama, llama.cpp) — reduces API cost/privacy concerns.
- Browser-use / desktop agents — agents that operate GUIs directly.
- Agent OS concepts — OS-level agent primitives.

## Gaps / Technologies to Investigate Further
- Evaluation frameworks (Ragas, LangSmith, TruLens) for research-report quality.
- Vector database selection for Atlas knowledge base retrieval.
- Scheduling/queuing for long-running research workflows.

## Sources
- LangChain/LangGraph documentation — https://langchain.com (2026)
- CrewAI documentation — https://docs.crewai.com (2026)
- AutoGen / Microsoft Agent Framework — Microsoft blog, "Designing Multi-Agent Intelligence", 2025-08-20 — https://developer.microsoft.com/blog/designing-multi-agent-intelligence/
- MDPI Systems survey, Zhu et al., 2026-06-01 — https://www.mdpi.com/1999-5903/18/6/326
- Google ADK guide — https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk, 2025-12-16
- Azure AI Agent design patterns — https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns, 2026-02-12
- Model Context Protocol — https://mcp.so (2025-2026)
- git-scm.com, git-worktree (2026)
