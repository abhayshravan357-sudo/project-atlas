# Agent A Report — Fundamentals

## Core Concepts

### Multi-Agent System (MAS)
A multi-agent system is composed of multiple autonomous agents (each typically backed by an LLM) with separate conversation contexts, coordinated through code, to solve problems beyond the reach of any single agent. The promise is specialization, parallelism, and bounded context per agent.

**Classification:** FACT
**Source:** HLD Handbook, "Multi-Agent Orchestration", 2026-05-11 — https://hld.handbook.academy/curriculum/ai-ml-system-design/multi-agent-orchestration

### Orchestrator-Worker Pattern
A lead agent (orchestrator) coordinates the process while delegating to specialized subagents (workers) that operate in parallel. User queries flow through the lead agent, which decomposes the query into subtasks and describes them to subagents. Each subagent needs an objective, output format, guidance on tools/sources, and clear task boundaries.

**Classification:** FACT
**Source:** Anthropic Engineering, "How we built our multi-agent research system", 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system

## Glossary / Terminology

| Term | Definition | Relevance to Atlas | Classification |
|------|------------|--------------------|----------------|
| Orchestrator | Central coordinating agent that decomposes tasks, delegates to workers, and synthesizes results. | The Main Agent of Atlas plays this role. | FACT |
| Worker / Subagent | Specialized agent assigned to an independent research domain; operates with bounded context. | Agents A–G are workers for cycle 1. | FACT |
| Agent | LLM-backed autonomous unit with tools, memory, and a defined role. | Core building block of Atlas. | FACT |
| Task / Assignment | A discrete unit of work delegated to an agent with objective and deliverables. | Each research domain is a task. | FACT |
| Delegation | The orchestrator assigning a task to a worker with context and boundaries. | How cycle 1 domains are assigned. | FACT |
| Worktree | A separate Git working tree attached to a branch, enabling isolated parallel work. | Each agent domain uses an isolated worktree. | FACT |
| Branch | A separate line of Git development isolating one agent's changes. | research/<domain> per agent. | FACT |
| Synthesis | The manager combining approved agent findings into a coherent knowledge base. | Core cycle 1 step. | FACT |
| Knowledge base | Organized repository of concepts, technologies, patterns, use cases, papers. | docs/knowledge-base/. | FACT |
| FACT | Claim supported by credible evidence with source link. | Atlas research standard. | PROPOSAL |
| INTERPRETATION | Conclusion derived from evidence. | Atlas research standard. | PROPOSAL |
| HYPOTHESIS | Idea requiring validation. | Atlas research standard. | PROPOSAL |
| PROPOSAL | Suggested direction for Atlas. | Atlas research standard. | PROPOSAL |

FACT/INTERPRETATION/HYPOTHESIS/PROPOSAL are the Atlas research-classification standard introduced as a project convention (PROPOSAL pending owner ratification).

## Prerequisites

### Git & Git Worktrees
**What:** Git version control; `git worktree` creates additional working trees linked to one repository, each on its own branch.
**Why it matters to Atlas:** Enables multiple agents to work in parallel on independent domains without conflicting file edits; keeps main clean.
**Requirements:** Git installed; a repository; separate working directories per worktree.
**Source:** Git documentation (git-worktree), standard tooling.

### LLM APIs / Providers
**What:** Programmatic access to large language models (Anthropic Claude, OpenAI GPT, Google Gemini, Groq, self-hosted/local models).
**Why it matters to Atlas:** Agents are LLM-backed; provider choice affects cost, latency, capability, and data privacy.
**Requirements:** API keys, rate-limit handling, model selection per task.
**Cost considerations:** Token usage scales with agent count; Anthropic reports multi-agent systems can use ~15× more tokens than single chat interactions.
**Source:** Anthropic Engineering, 2025-06-13.

### Orchestration Frameworks
**What:** Libraries providing agent primitives, coordination patterns, state management, and tool use (LangGraph, LangChain, CrewAI, AutoGen/Microsoft Agent Framework, Google ADK, OpenAI Swarm/Agents SDK).
**Why it matters to Atlas:** Reduces custom orchestration code; provides patterns for delegation, evaluation, and human-in-the-loop.
**Requirements:** Framework installation, LLM provider integration, prompt engineering.
**Source:** Framework documentation; Azure AI Agent design patterns, 2026-02-12.

### CLI Tooling
**What:** Command-line interface framework (Click, Typer, Ink, Commander) for running research cycles and managing agents.
**Why it matters to Atlas:** Atlas is positioned as a CLI/orchestration tool; CLI is the primary operator interface.
**Requirements:** Command structure, output formatting, error handling.
**Source:** Standard CLI library documentation.

## Research Cycle Phases

| Phase | Description |
|-------|-------------|
| PLAN | Define objectives and research questions. |
| DELEGATE | Create branches/worktrees; assign specialized agents with detailed prompts. |
| INVESTIGATE | Agents research and create deliverables in isolation. |
| REPORT | Agents submit findings and completion reports. |
| REVIEW | Main Agent checks quality; assigns APPROVED / REVISION REQUIRED / EXPAND / REJECTED. |
| SYNTHESIZE | Manager combines approved discoveries into knowledge base. |
| COMMIT | Manager stages/commits approved work and merges branches into main. |
| REASSESS | Manager identifies new directions; plans next cycle. |

**Source:** Project Atlas operational standard (this document), derived from the orchestrator-worker pattern.

## Advanced Foundations

### Agent Communication Protocols
Agents exchange information through structured protocols. Emerging standards include Model Context Protocol (MCP) for tool/context sharing and Agent-to-Agent (A2A) for inter-agent communication. No widely adopted benchmark targets orchestration evaluation.

**Classification:** FACT (MCP/A2A existence), INTERPRETATION (benchmark gap)
**Source:** MDPI Systems survey, "LLM-Based Multi-Agent Orchestration", 2026-06-01 — https://www.mdpi.com/1999-5903/18/6/326

### Shared State / Session State
Coordination via shared state (e.g., ADK's session.state with output_key) lets the next agent pick up where the prior left off. Centralized state simplifies flow but creates information-flow bottlenecks.

**Classification:** FACT
**Source:** Google ADK developer's guide, 2025-12-16.

### Memory
Short-term (within-session context) and long-term (persistent knowledge base/vector store) memory. Bounded context per agent is a core benefit of multi-agent design.

**Classification:** FACT
**Source:** HLD Handbook, 2026-05-11.

### Evaluation (LLM-as-Judge)
Research outputs are difficult to evaluate programmatically. A single LLM call outputting scores 0.0–1.0 plus pass/fail was found most consistent with human judgement.

**Classification:** FACT
**Source:** Anthropic Engineering, 2025-06-13.

### Tool Use
Agents call tools (search, read, write, git) to gather information and store work in external systems, passing lightweight references back to the coordinator.

**Classification:** FACT
**Source:** Anthropic Engineering, 2025-06-13.

### Human-in-the-Loop
The manager reviews agent reports before integration; human oversight required for irreversible changes, publishing, spending, and architectural commitments.

**Classification:** PROPOSAL (Atlas project convention)

## Open Questions / What Remains Unknown
- Which orchestration framework best fits Atlas's git-worktree-based parallel research model? (frameworks assume in-process agents; Atlas uses isolated filesystem worktrees — mismatch to investigate)
- How to evaluate research report quality reliably at scale without excessive LLM-as-judge cost?
- What is the optimal balance between parallel independent research paths vs. role-centric handoffs (which risk a "telephone game" fidelity loss)?

## Sources
- Anthropic Engineering, "How we built our multi-agent research system", 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
- MDPI Systems, "LLM-Based Multi-Agent Orchestration: A Survey", Zhu et al., 2026-06-01 — https://www.mdpi.com/1999-5903/18/6/326
- Google Developers Blog, "Developer's guide to multi-agent patterns in ADK", 2025-12-16 — https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk
- Microsoft Learn, "AI Agent Orchestration Patterns - Azure Architecture Center", 2026-02-12 — https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- Microsoft for Developers, "Designing Multi-Agent Intelligence", 2025-08-20 — https://developer.microsoft.com/blog/designing-multi-agent-intelligence/
- HLD Handbook, "Multi-Agent Orchestration", 2026-05-11 — https://hld.handbook.academy/curriculum/ai-ml-system-design/multi-agent-orchestration
- Git documentation, git-worktree — https://git-scm.com/docs/git-worktree
