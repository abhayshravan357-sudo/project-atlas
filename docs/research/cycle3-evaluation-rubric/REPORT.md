# Agent N Report — Cycle 3 Evaluation Rubric

## Objective
Produce a concrete, implementable evaluation rubric and LLM-as-judge prompt for assessing research-report quality in Project Atlas, with a hybrid human + automated evaluation model.

## Context
Cycle 2 recommended LLM-as-judge for initial screening plus human manager review as the final gate. Cycle 3 specifies the rubric, judge prompt, scoring, and integration point.

## Evaluation Dimensions

| Dimension | Weight | Description | Evidence required |
|-----------|--------|-------------|-------------------|
| Accuracy | 25% | Claims supported by credible sources with links and dates | Source citations per claim |
| Completeness | 20% | All research questions addressed; no major gaps | Coverage of assignment questions |
| Source quality | 20% | Tier 1/2/3 sources; primary sources preferred | Source registry; source tiers |
| Synthesis | 15% | Findings combined coherently; contradictions noted | Integrated narrative; contradiction handling |
| Classification | 10% | FACT/INTERPRETATION/HYPOTHESIS/PROPOSAL labeled correctly | Labels on all claims |
| Citation correctness | 10% | Links resolve; dates present; format consistent | Link audit; date format |

Total: 100%

## Scoring Model
- Each dimension scored 0.0–1.0 by the LLM judge
- Weighted overall score = Σ(dimension_score × weight)
- Pass threshold: ≥ 0.75 overall AND no dimension below 0.50
- Below threshold → REVISION REQUIRED with specific feedback

## LLM-as-Judge Prompt (template)

```
You are an evaluation judge for Project Atlas research reports.

Evaluate the following research report against these dimensions:
1. Accuracy (0.0-1.0): Are claims supported by credible sources with links and dates?
2. Completeness (0.0-1.0): Are all research questions addressed?
3. Source quality (0.0-1.0): Are sources Tier 1/2/3; primary sources preferred?
4. Synthesis (0.0-1.0): Are findings combined coherently; are contradictions noted?
5. Classification (0.0-1.0): Are FACT/INTERPRETATION/HYPOTHESIS/PROPOSAL labels correct?
6. Citation correctness (0.0-1.0): Do links resolve? Are dates present?

Weights: Accuracy 25%, Completeness 20%, Source quality 20%, Synthesis 15%, Classification 10%, Citation correctness 10%.

Report to evaluate:
{report_content}

Return your evaluation as JSON:
{
  "dimensions": {
    "accuracy": {"score": 0.0-1.0, "reasoning": "..."},
    "completeness": {"score": 0.0-1.0, "reasoning": "..."},
    "source_quality": {"score": 0.0-1.0, "reasoning": "..."},
    "synthesis": {"score": 0.0-1.0, "reasoning": "..."},
    "classification": {"score": 0.0-1.0, "reasoning": "..."},
    "citation_correctness": {"score": 0.0-1.0, "reasoning": "..."}
  },
  "overall_score": 0.0-1.0,
  "pass_threshold": 0.75,
  "pass": true/false,
  "revision_feedback": "specific actionable feedback if revision required",
  "dimension_below_minimum": ["dimension names below 0.50"]
}
```

## Hybrid Evaluation Model

| Stage | Evaluator | Role | Outcome |
|-------|-----------|------|---------|
| Stage 1 | LLM-as-judge | Score report against rubric; flag issues | Pass / Revision required |
| Stage 2 | Human manager | Review LLM-as-judge result; final APPROVED / REVISION REQUIRED / REJECTED | Final decision |

The human manager reviews Stage 1 output rather than re-scoring from scratch, reducing human effort while retaining quality control.

## Integration with LangGraph
The evaluation occurs at the `review` node (LangGraph interrupt):
1. Orchestrator runs LLM-as-judge on synthesized output
2. `interrupt()` presents score + feedback to manager
3. Manager: APPROVE → commit; REVISE → route back with feedback; REJECT → terminate

## Source Tier Definitions
| Tier | Definition | Examples |
|------|-----------|----------|
| Tier 1 | Primary evidence: original research papers, official docs, standards, verified specs | arXiv papers, LangGraph docs, git-scm.com |
| Tier 2 | Strong secondary: peer-reviewed surveys, institutional reports, detailed technical analyses | MDPI Systems survey, Azure AI patterns |
| Tier 3 | Supporting: engineering articles, technical blogs, community experience | Engineering blogs, framework tutorials |
| Tier 4 | Discovery leads: unverified claims, informal discussions | Search snippets, forum posts (not for factual claims) |

## Cost of Evaluation
LLM-as-judge adds one judge call per report (~500-1500 tokens). At cycle scale (5-10 reports), cost is negligible (<$1). At scale (100+ reports), evaluate sampling or cheaper judge model.

**Classification:** Estimate

## Success Criteria
- Rubric covers all 6 dimensions with weights
- Judge prompt is complete and copy-paste ready
- Hybrid model defined with clear stage responsibilities
- LangGraph integration point identified
- Source tiers defined
- Cost estimated

## Open Questions
- What judge model balances cost and reliability?
- How often should the rubric be recalibrated against human judgments?
- Should Stage 2 (human) review all reports or only borderline ones?

## Sources
- Anthropic Engineering, multi-agent research system (LLM-as-judge), 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
- Azure AI Agent design patterns (human-in-the-loop), 2026-02-12 — https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- Agent K Report — Cycle 2 Evaluation Framework (this repo)
- LangGraph documentation — https://langchain.com (2026)
