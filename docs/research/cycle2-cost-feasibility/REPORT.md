# Agent L Report — Cycle 2 Cost & Feasibility Modeling

## Token Cost Drivers

| Driver | Effect on cost |
|--------|---------------|
| Agent count | More agents = more total tokens (parallel generation) |
| Turns per agent | More reasoning/tool-calling turns = more tokens |
| Context length | Longer prompts and histories = more tokens per call |
| Judge model (LLM-as-judge) | Additional evaluation tokens per report |
| Model selection | Capable models cost more per token than cheaper ones |

**Source:** Anthropic Engineering, multi-agent research system, 2025-06-13 (~15× tokens for multi-agent vs single chat; ~4× for agents vs chat).

## Cost Estimation Table

| Scale | Agents | Tokens/cycle (est.) | Cost/cycle (est., $) | Time/cycle | Notes |
|-------|--------|---------------------|----------------------|------------|-------|
| Small | 3–5 | 500K–1M | $2.50–$10 | 1–2 hours | Cycle 1-sized research |
| Medium | 6–12 | 2M–5M | $10–$50 | 3–6 hours | Multiple domains |
| Large | 13–25+ | 8M–20M+ | $40–$200+ | 6+ hours | Broad discovery |

**Classification:** Estimates. Based on Anthropic token-cost data and typical LLM pricing (~$1–$5 per 1M input tokens, ~$3–$15 per 1M output tokens). Actual costs vary by provider and model.

## Compute and Storage Cost Analysis

### Local CLI (current model)
- Compute: minimal (agent execution on local machine; LLM inference via API)
- Storage: minimal (git repos + knowledge base, MBs to GBs)
- Cost: near-zero infrastructure; LLM API cost dominates

### Cloud / containerized
- Compute: VM/container runtime for agents; higher cost
- Storage: persistent volumes for knowledge base; higher
- Cost: infrastructure + LLM API; justified only if scale requires it

**Classification:** INTERPRETATION

## Developer Time Estimate

| Activity | Estimate |
|----------|----------|
| Build orchestrator (CLI + worktree management) | 2–4 weeks |
| Agent glue (framework-to-worktree integration) | 1–2 weeks |
| Evaluation (LLM-as-judge rubrics) | 1 week |
| Ongoing maintenance | 5–10 hours/week |

**Classification:** Estimate

## Break-Even vs Manual Research

Atlas is cost-justified when: (breadth × depth × frequency) exceeds manual research cost. For one-off research, manual is cheaper. For recurring multi-domain research, Atlas saves time despite token costs. Break-even depends on researcher hourly rate vs token cost.

**Classification:** INTERPRETATION

## Cost Mitigation Strategies

1. **Model selection:** Use cheaper models for routine tasks; reserve capable models for synthesis and review.
2. **Parallelization limits:** Only parallelize truly independent tasks; don't force parallelism.
3. **Caching:** Cache repeated LLM calls and search results.
4. **Context management:** Summarize between phases; trim long histories.
5. **Selective evaluation:** Apply LLM-as-judge only where quality risk is high.

## Feasibility Assessment

| Scale | Feasible? | Conditions |
|-------|-----------|------------|
| Small | Yes | Low token cost; local CLI; cycle 1 scope |
| Medium | Yes | Cost mitigation required; manager review gate |
| Large | Conditional | Needs infrastructure budget; efficiency optimizations |

**Go/no-go conditions:** Proceed if token cost per cycle is acceptable to the project owner relative to manual research cost. Re-evaluate before scaling beyond medium.

## Sources
- Anthropic Engineering, multi-agent research system, 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
- Azure AI Agent design patterns, 2026-02-12 — https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
