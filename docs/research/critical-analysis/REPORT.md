# Agent G Report — Critical Analysis

## Technical Limitations

| Limitation | Impact | Mitigations | Evidence |
|------------|--------|-------------|----------|
| Coordination overhead | More tokens, latency, complexity than single agent | Limit agent count; parallelize only independent tasks | Anthropic: multi-agent ~15× tokens of chat; agents ~4× chat, 2025-06-13 |
| Context-window bounds | Long research threads risk context loss | Summarize; persistent knowledge base; handoff references | HLD Handbook: bounded context per agent, 2026-05-11 |
| Non-determinism | LLM outputs vary; research results not reproducible | Temperature control; fixed seeds where supported; evaluation | Interpretation |
| DAG trace debugging | Multi-agent traces are DAGs, not trees; harder to debug | Structured logging; tracing tools; checkpoints | HLD Handbook, 2026-05-11 |
| Parallelization limits | Not all tasks parallelize; some are sequential | Identify parallelizable vs sequential phases; don't force parallelism | Anthropic, 2025-06-13 |

## Security Issues

| Threat | Impact | Mitigations | Evidence |
|--------|--------|-------------|----------|
| Agent access to repos/secrets | Agents may read/modify sensitive code or leak secrets | Scoped permissions; no secrets in repos; review before commit | Interpretation |
| Prompt injection via tool outputs | Malicious tool output manipulates agent behavior | Sanitize tool outputs; restrict agent tool scope | Interpretation |
| Tool-use vulnerabilities | Agents with file/git access can cause damage | Least-privilege; read-only where possible; worktree isolation | Interpretation |
| Supply chain (frameworks/providers) | Compromised LLM provider or framework | Pin dependencies; audit frameworks; use reputable providers | Interpretation |

## Cost Analysis

| Cost component | Estimate | Notes |
|----------------|----------|-------|
| LLM token cost | High | Multi-agent ~15× single chat; scales with agent count and turns |
| Compute | Low-Medium | Local CLI minimal; cloud agents higher |
| Storage | Low | Git repos + knowledge base |
| Developer time | Medium | Building/maintaining orchestrator, reviewing reports |

**Source:** Anthropic Engineering, 2025-06-13 (token cost). Other estimates are Interpretation.

## Feasibility Problems

| Problem | Impact | Mitigations | Evidence |
|---------|--------|-------------|----------|
| Long-running workflows | State loss, timeouts | Checkpoints/persistence (LangGraph); resume capability | LangChain docs |
| State consistency | Agents working on stale/conflicting state | Worktree isolation; single source of truth (git); merge review | Atlas design |
| Evaluation at scale | Research quality hard to assess programmatically | LLM-as-judge; human review gate | Anthropic, 2025-06-13 |
| Framework lock-in | Tied to one orchestration framework | Abstract orchestration layer; choose portable patterns | Interpretation |

## Dependencies and Lock-in Risks

- LLM provider APIs (Anthropic, OpenAI, Google): cost, availability, rate limits, data privacy.
- Orchestration framework choice: LangGraph/AutoGen/ADK each have ecosystem lock-in.
- Git workflow assumptions: agents comfortable with CLI/git; not accessible to non-technical users.

## Failure Modes

| Trigger | Impact | Detection | Mitigation |
|---------|--------|-----------|------------|
| Agent infinite loop | Token burn, no progress | Iteration limits; timeout | Set iteration limits (Azure guidance) |
| Context loss | Incoherent research output | Review gate; summarization | Persistent knowledge base |
| Conflicting research | Contradictory findings across agents | Synthesis review; contradiction detection | Manager review |
| Integration breakage | Tool/API changes break agents | Pin versions; monitor providers | Dependency pinning |
| Merge conflicts | Blocked integration | Conflict detection in CI | Careful branch management; sequential merge |

## Approaches That Appear Impractical

| Approach | Why impractical |
|----------|-----------------|
| Fully autonomous research, no human review | Quality/safety risk; violates human-oversight principle |
| Thousands of concurrent agents | Token cost prohibitive (~15× chat); coordination infeasible |
| GUI-driven agents for primary research | Fragile, slow, unreliable vs APIs |
| Decentralized P2P as sole orchestration | No central synthesis point; hard to trace research (Matrix is for synthetic data, not research synthesis) |

## Assumptions Needing Testing

1. Git worktrees are an effective isolation primitive for LLM agents (most frameworks assume in-process agents).
2. LLM-as-judge can reliably evaluate research-report quality at acceptable cost.
3. Parallel independent research paths produce better synthesis than role-centric handoffs for broad discovery.
4. The orchestrator-worker pattern scales to the number of domains Atlas needs without becoming a bottleneck.

## Risk Matrix

| Risk | Category | Likelihood | Impact | Mitigations | Evidence |
|------|----------|------------|--------|-------------|----------|
| High token cost | Cost | High | High | Limit agents; parallelize only independent tasks | Anthropic 2025-06-13 |
| Agent infinite loop | Reliability | Medium | Medium | Iteration limits; timeouts | Azure AI patterns 2026-02-12 |
| Secret leakage | Security | Medium | High | Scoped permissions; no secrets in repos | Interpretation |
| Framework lock-in | Dependency | Medium | Medium | Abstract layer; portable patterns | Interpretation |
| Poor research quality | Quality | Medium | High | Human review gate; LLM-as-judge | Anthropic 2025-06-13 |
| Context loss | Reliability | Medium | Medium | Summarization; persistent KB | HLD Handbook 2026-05-11 |

## Sources
- Anthropic Engineering, "How we built our multi-agent research system", 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
- Azure AI Agent design patterns, 2026-02-12 — https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- HLD Handbook, "Multi-Agent Orchestration", 2026-05-11 — https://hld.handbook.academy/curriculum/ai-ml-system-design/multi-agent-orchestration
- MDPI Systems survey, Zhu et al., 2026-06-01 — https://www.mdpi.com/1999-5903/18/6/326
