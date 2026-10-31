# Agent Assignment — Technology Researcher (Agent B)

## Agent Identity
- ID: B
- Name: Agent B
- Role: Technology Researcher
- Branch: research/technology-landscape
- Worktree: /tmp/atlast-wt/technology-landscape

## Research Objective
Investigate languages, frameworks, libraries, platforms, tools, APIs, and emerging technologies that could support Atlas. For each promising technology, cover: what it does, how it works, why it matters, where it is used, advantages, disadvantages, requirements, dependencies, complexity, cost considerations, security considerations, alternatives, and relevance to Atlas. Do NOT decide direction, do NOT write code, do NOT commit to Git.

## Scope
Languages, orchestration frameworks, platforms/tools, emerging technologies, maturity assessment.

## Questions to Investigate
1. Languages: Python, TypeScript/JavaScript, Go, Rust — suitability for agent orchestration (ecosystem, LLM library support, concurrency, deployment).
2. Orchestration frameworks: LangGraph, LangChain, CrewAI, AutoGen (Microsoft Agent Framework / Semantic Kernel merge), Google Agent Development Kit (ADK), OpenAI Swarm, OpenAI Agents SDK. For each: core model, how it coordinates agents, strengths, weaknesses.
3. Platforms/tools: git & git worktrees, CLI frameworks (Click, Typer, Ink, Commander), vector databases, scheduling/queuing, LLM provider APIs (Anthropic, OpenAI, Google, Groq, local models).
4. Emerging technologies: Model Context Protocol (MCP), Agent-to-Agent (A2A) protocol, browser-use / desktop agents, agent OS concepts, local-first model execution.
5. Which technologies are mature vs experimental? Which have active communities and credible backing?

## Expected Depth
For each technology, a structured profile. Target a comparison table plus ~6-10 technology profiles (~1000-1400 words).

## Research Methodology
Official documentation, GitHub repositories, engineering blogs, framework docs. Cite sources with links and dates. Distinguish FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL. Do not fabricate features, benchmarks, or capabilities. State insufficient evidence explicitly.

## Required Output Files
Return report as Markdown covering:
- # Agent B Report — Technology Landscape
- Technology Comparison Matrix (table: technology, category, what it does, maturity, key strengths, key weaknesses, relevance to Atlas, source)
- Individual technology profiles (6-10): what/how/why/where-used, advantages, disadvantages, requirements, dependencies, complexity, cost, security, alternatives, relevance to Atlas
- Languages assessment
- Emerging tech watchlist
- Gaps / technologies to investigate further
- Sources (links + dates)

## Evidence Requirements
Every important claim must carry a source link and date, or be labeled HYPOTHESIS/INTERPRETATION.

## Restrictions
- No application code.
- No Git commits/merges/pushes.
- Do not modify main branch.
- Do not write files to disk (return report in response); the Main Agent will place reports.
- Do not commit Atlas to a single technology stack.

## Completion Criteria
Report returned with comparison matrix + multiple tech profiles, each with advantages/disadvantages/complexity/cost/security, source-cited, FACT/INTERP/HYPOTH/PROPOSAL labeled.
