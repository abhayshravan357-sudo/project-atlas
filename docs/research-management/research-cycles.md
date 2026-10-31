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

## Cycle 3 — Prototype Design & Validation (Complete)

Objective: Validate the core architecture and cost model with concrete designs.

Assignments completed (4):
1. Agent M — Prototype design: LangGraph orchestrator-worker graph + git worktree manager + human-in-the-loop review gate specified
2. Agent N — Evaluation rubric: 6-dimension rubric (accuracy 25%, completeness 20%, source quality 20%, synthesis 15%, classification 10%, citation 10%), LLM-as-judge prompt, hybrid human+automated model
3. Agent O — MCP integration: filesystem/git/search/LLM/knowledge-base MCP servers; stdio+HTTP transport; worktree-scoped sandboxing
4. Agent P — Cost validation: real provider pricing; small/medium/large cost estimates; cost mitigation strategies; break-even vs manual research

Status: All 4 reports reviewed APPROVED, merged into `main`.

Key cycle 3 findings:
- Prototype: LangGraph StateGraph with plan/delegate/investigate/report/synthesize/review/commit nodes; LangGraph interrupt for manager review
- Rubric: weighted 0.0-1.0 scoring with 0.75 pass threshold; LLM-as-judge + human manager gate
- MCP: 5 servers (filesystem, git, search, LLM, KB); stdio for local, HTTP for remote; worktree-scoped sandboxing
- Cost: small cycle ~$45-$210 depending on model; break-even favors Atlas at small/medium scale

## Cycle 4 — Prototype Implementation (Planned)

Objective: Build and validate a working prototype.

Planned assignments:
1. Prototype implementation: worktree manager + LangGraph orchestrator skeleton
2. Rubric calibration: test LLM-as-judge against human judgments on sample reports
3. MCP build: filesystem + git servers scoped to worktrees
4. Cost measurement: run prototype cycle, measure real token usage
