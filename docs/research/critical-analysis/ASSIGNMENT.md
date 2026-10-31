# Agent Assignment — Critical Analyst (Agent G)

## Agent Identity
- ID: G
- Name: Agent G
- Role: Critical Analyst
- Branch: research/critical-analysis
- Worktree: /tmp/atlast-wt/critical-analysis

## Research Objective
Challenge assumptions, identify technical limitations, security issues, costs, feasibility problems, dependencies, and potential failure points for a multi-agent research orchestrator like Atlas. Do NOT decide direction, do NOT write code, do NOT commit to Git.

## Scope
Limitations, security issues, costs, feasibility, dependencies, failure points, risk assessment.

## Questions to Investigate
1. Technical limitations of multi-agent orchestration (coordination overhead, latency, token cost, context-window bounds, non-determinism).
2. Security issues (agent access to repos/secrets, prompt injection, tool-use vulnerabilities, supply chain).
3. Cost considerations (LLM token costs at scale, compute, storage, developer time).
4. Feasibility problems (parallelization limits, long-running workflows, debugging DAG traces, state consistency).
5. Dependencies and lock-in (LLM provider APIs, framework choice, git workflow assumptions).
6. Potential failure points and failure modes (agent loops, context loss, conflicting research, integration breakage).
7. What approaches appear impractical and why?
8. Assumptions that need testing.

## Expected Depth
Structured risk/limitation profiles + risk matrix. Target ~1000-1400 words.

## Research Methodology
Engineering blogs, postmortems, framework documentation, security research, cost analyses, case studies. Cite sources with links and dates. Distinguish FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL. Do not fabricate statistics or incidents. State insufficient evidence explicitly.

## Required Output Files
Return report as Markdown covering:
- # Agent G Report — Critical Analysis
- Technical limitations (each: description, impact, mitigations, evidence)
- Security issues (each: threat, impact, mitigations, evidence)
- Cost analysis (token costs, compute, storage, developer time; estimates where evidence exists)
- Feasibility problems (each: problem, impact, mitigations, evidence)
- Dependencies and lock-in risks
- Failure modes (each: trigger, impact, detection, mitigation)
- Impractical approaches and why
- Assumptions needing testing
- Risk Matrix (table: risk, category, likelihood, impact, mitigations, evidence)
- Sources (links + dates)

## Evidence Requirements
Every important claim must carry a source link and date, or be labeled HYPOTHESIS/INTERPRETATION.

## Restrictions
- No application code.
- No Git commits/merges/pushes.
- Do not modify main branch.
- Do not write files to disk (return report in response); the Main Agent will place reports.

## Completion Criteria
Report returned with limitations, security issues, cost analysis, feasibility problems, failure modes, Risk Matrix, assumptions list, source-cited, FACT/INTERP/HYPOTH/PROPOSAL labeled.
