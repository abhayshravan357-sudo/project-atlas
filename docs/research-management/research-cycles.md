# Research Cycles — Project Atlas

## Cycle 1 — Broad Discovery (Complete)

Objective: Map possible directions for Project Atlas across fundamentals, technology, architecture, applications, academic literature, innovation, and critical analysis.

Status: All 7 domains researched, reviewed APPROVED, merged into `main`.

Key findings:
- Orchestrator-worker is the dominant pattern for research orchestration (Anthropic, 2025; Azure AI patterns, 2026)
- Git worktrees provide strong isolation for parallel agent domains
- LangGraph / LangChain / AutoGen (Microsoft Agent Framework) / Google ADK are the main orchestration framework candidates
- Python is the default language for agent orchestration
- MCP (tool integration) and A2A (inter-agent) are emerging standards to watch
- Multi-agent systems cost ~15× more tokens than single chat (cost risk)
- No open-source tool combines git-worktree isolation with multi-agent research cycles (opportunity)

## Cycle 2 — Deep Dives (Complete)

Objective: Validate the most promising architecture and technology choices from Cycle 1.

Assignments completed (5 independent subagent domains):
1. Agent H — Architecture deep-dive: orchestrator-worker + git worktree model validated; recommendations for framework glue and worker-count limits
2. Agent I — Technology comparison: LangGraph recommended (graph model, persistence, human-in-the-loop); ADK secondary; AutoGen not recommended for cycle 2
3. Agent J — Integration protocols: adopt MCP for tool access; do not adopt A2A in cycle 2 (too early)
4. Agent K — Evaluation framework: hybrid LLM-as-judge + human manager review recommended
5. Agent L — Cost & feasibility: small/medium scale feasible; cost mitigation strategies documented

Status: All 5 reports reviewed APPROVED, merged into `main`.

Key cycle 2 findings:
- LangGraph best fits the research-cycle graph model with cycles and native human-in-the-loop interrupts
- Git worktrees are feasible but require custom framework glue (frameworks assume in-process agents)
- MCP is the integration protocol to watch; A2A is too immature
- LLM-as-judge + human review is the recommended evaluation model
- Cost is feasible at small/medium scale with mitigation strategies

## Cycle 3+ — Validation & Direction (Future)

- Feasibility prototype of orchestrator-worker + git worktree model
- Evaluation rubric implementation and testing
- MCP server prototype for agent tool access
- Cost model validation with real LLM usage
- Architecture commitment decision
- Go / no-go on implementation
