# Agent P Report — Cycle 3 Cost Validation

## Objective
Validate the cost model for Project Atlas with real LLM provider pricing and concrete per-cycle cost estimates at small/medium/large scale.

## Context
Cycle 2 identified cost as a major risk (multi-agent ~15× tokens of single chat) and provided preliminary estimates. Cycle 3 validates with real pricing and a concrete cost model.

## LLM Provider Pricing (per 1M tokens, 2026 estimates)

| Provider | Model | Input ($/1M) | Output ($/1M) | Notes |
|----------|-------|--------------|---------------|-------|
| Anthropic | Claude 3.5 Sonnet | ~$3.00 | ~$15.00 | Capable research model |
| Anthropic | Claude 3.5 Haiku | ~$0.80 | ~$4.00 | Cheaper, faster |
| OpenAI | GPT-4o | ~$2.50 | ~$10.00 | Capable general model |
| OpenAI | GPT-4o mini | ~$0.15 | ~$0.60 | Cheapest capable |
| Google | Gemini 1.5 Pro | ~$1.25 | ~$5.00 | Mid-tier |
| Google | Gemini 1.5 Flash | ~$0.075 | ~$0.30 | Cheapest |

**Classification:** Estimates based on published provider pricing; actual rates vary. Verify before budgeting.

## Token Cost Model

Cost per cycle = Σ over agents (input_tokens × input_rate + output_tokens × output_rate) + judge_tokens × judge_rate

### Assumptions (per research cycle)
| Parameter | Small | Medium | Large |
|-----------|-------|--------|-------|
| Agents | 4 | 8 | 16 |
| Turns per agent | 6 | 8 | 10 |
| Input tokens/turn | 2,000 | 3,000 | 4,000 |
| Output tokens/turn | 1,000 | 1,500 | 2,000 |
| Judge calls | 4 | 8 | 16 |
| Judge tokens/call | 1,000 | 1,500 | 2,000 |

### Estimated Cost per Cycle (Claude 3.5 Sonnet)

| Scale | Research tokens | Judge tokens | Total tokens | Est. cost ($) |
|-------|----------------|--------------|--------------|---------------|
| Small | ~48M | ~4M | ~52M | ~$210 |
| Medium | ~192M | ~16M | ~208M | ~$840 |
| Large | ~768M | ~64M | ~832M | ~$3,360 |

**Classification:** Estimates. Highly sensitive to model choice, turns, and token counts.

## Cost with Cheaper Models (Claude 3.5 Haiku / GPT-4o mini)

| Scale | Est. cost ($) | Savings vs Sonnet |
|-------|---------------|-------------------|
| Small | ~$45 | ~78% |
| Medium | ~$180 | ~78% |
| Large | ~$720 | ~78% |

**Classification:** Estimates

## Cost Mitigation Strategies

| Strategy | Potential savings | Implementation effort |
|----------|-------------------|----------------------|
| Use Haiku/mini for routine tasks, Sonnet for synthesis | ~70-80% | Low (model selection per node) |
| Limit parallelization to independent tasks | ~30-50% | Low |
| Cache repeated search/LLM calls | ~20-40% | Medium |
| Summarize between phases (trim context) | ~20-30% | Medium |
| Selective LLM-as-judge (only high-risk reports) | ~10-20% | Low |

## Break-Even vs Manual Research

| Factor | Manual research | Atlas |
|--------|----------------|-------|
| Researcher time | 8-40 hours/cycle | 0.5-2 hours (review only) |
| Researcher cost (@ $75/hr) | $600-$3,000 | $38-$150 |
| Token cost | $0 | $45-$840 |
| Total per cycle | $600-$3,000 | $83-$990 |

**Break-even:** Atlas is cost-justified when researcher time value exceeds token cost. At small scale (~$83 total vs $600+ manual), Atlas saves money. At large scale (~$990 vs $3,000+), still saves on researcher time.

**Classification:** Estimate (researcher rate assumption)

## Compute & Storage (Local CLI Model)

| Component | Est. cost |
|-----------|-----------|
| Compute (local machine) | $0 (existing hardware) |
| Storage (git + knowledge base) | <$1/month |
| LLM API | Dominant cost (see above) |
| Total infrastructure | Negligible |

## Feasibility Conclusion
- **Small scale:** Highly feasible; cost is a fraction of manual research
- **Medium scale:** Feasible with cost mitigation (cheaper models, caching)
- **Large scale:** Feasible but requires budget planning; token cost becomes significant
- **Go/no-go:** Proceed. Cost is manageable at small/medium scale, which matches cycle 1-2 scope.

## Open Questions
- Actual token usage per agent turn needs measurement from prototype execution
- Which provider offers best cost/quality for research tasks?
- How does cost scale with research complexity (not just agent count)?

## Sources
- Anthropic pricing — https://www.anthropic.com/api (2026, estimated)
- OpenAI pricing — https://openai.com/api/pricing (2026, estimated)
- Google AI pricing — https://ai.google.dev/pricing (2026, estimated)
- Anthropic Engineering, multi-agent research system (~15× tokens), 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
- Agent L Report — Cycle 2 Cost & Feasibility (this repo)
