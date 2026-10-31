# Agent Assignment — Architecture Researcher (Agent C)

## Agent Identity
- ID: C
- Name: Agent C
- Role: Architecture Researcher
- Branch: research/architecture
- Worktree: /tmp/atlast-wt/architecture

## Research Objective
Investigate alternative system architectures, design patterns, integrations, scalability, modularity, and deployment approaches relevant to an agent research orchestrator. Do NOT assume a single architecture; compare multiple. Do NOT decide direction, do NOT write code, do NOT commit to Git.

## Scope
Orchestration patterns, centralized vs decentralized, integration patterns, scalability, modularity, deployment approaches.

## Questions to Investigate
1. Orchestration patterns: orchestrator-worker, sequential/pipeline, hierarchical, coordinator-dispatcher (concierge), handoff (peer-to-peer), group chat, swarm. For each: how it works, best for, watch out for.
2. Centralized vs decentralized orchestration: trade-offs (bottleneck vs complexity, coordination overhead).
3. Integration patterns: Model Context Protocol (MCP), Agent-to-Agent (A2A), REST APIs, message queues, shared state/session state, tool exposure.
4. Scalability considerations: parallelization limits (not all tasks parallelize), context-window bounds per agent, token cost, latency, long-running workflows, debugging DAG traces (not trees).
5. Modularity: separating plan/delegate/investigate/report/review/synthesize/commit/reassess into independent modules; independent research paths vs role-centric (planner/implementer/tester/reviewer) "telephone game" risk.
6. Deployment approaches: local CLI with git worktrees, containerized, cloud, hybrid.
7. Which architectures suit "research-first" (many parallel independent directions) vs "implementation" (tight dependencies)?

## Expected Depth
For each architecture/pattern, description + how it works + pros/cons + complexity + suitability for Atlas + example. Target an architecture comparison matrix + ~6-8 pattern descriptions (~1000-1400 words). Include a Mermaid diagram description (text) for at least one candidate architecture.

## Research Methodology
Architecture docs (Azure AI Agent design patterns, Microsoft Learn orchestrator/subagent, Google ADK patterns, Anthropic multi-agent research system, HLD Handbook, arXiv surveys). Cite sources with links and dates. Distinguish FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL. Do not fabricate. State insufficient evidence explicitly.

## Required Output Files
Return report as Markdown covering:
- # Agent C Report — System Architecture
- Orchestration pattern catalog (each: description, how it works, best for, watch out for, complexity, Atlas suitability)
- Centralized vs decentralized comparison
- Integration patterns (MCP, A2A, APIs, queues, shared state)
- Scalability analysis (parallelization limits, context window, token cost, latency, DAG trace debugging)
- Modularity analysis (independent research paths vs role-centric; telephone game risk)
- Deployment approaches (local worktree CLI, container, cloud, hybrid)
- Architecture Comparison Matrix (table: pattern, coordination, routing, best for, watch out for, complexity, Atlas fit)
- Candidate architecture(s) for Atlas with Mermaid text diagram
- Sources (links + dates)

## Evidence Requirements
Every important claim must carry a source link and date, or be labeled HYPOTHESIS/INTERPRETATION.

## Restrictions
- No application code.
- No Git commits/merges/pushes.
- Do not modify main branch.
- Do not write files to disk (return report in response); the Main Agent will place reports.
- Do not commit Atlas to one architecture.

## Completion Criteria
Report returned with pattern catalog, comparison matrix, scalability/modularity analysis, deployment options, Mermaid diagram text, source-cited, FACT/INTERP/HYPOTH/PROPOSAL labeled.
