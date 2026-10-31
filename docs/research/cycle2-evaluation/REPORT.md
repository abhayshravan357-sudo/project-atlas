# Agent K Report — Cycle 2 Evaluation Framework

## LLM-as-Judge Analysis

### What it is
LLM-as-judge uses an LLM to evaluate the quality of another LLM's output, typically producing a score (0.0–1.0) and/or a pass/fail grade.

**Classification:** FACT
**Source:** Anthropic Engineering, "How we built our multi-agent research system", 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system

### How it works
A judge LLM is prompted with the candidate output and rubric; it returns a score and/or pass/fail. Anthropic found a single LLM call with 0.0–1.0 scoring plus pass/fail was most consistent with human judgement, especially for clear-answer test cases.

### Reliability vs human judgement
Anthropic reports this method was consistent with human judgements and scalable to hundreds of outputs. However, reliability decreases for ambiguous or open-ended outputs (like research reports) where there is no single correct answer.

**Classification:** FACT (Anthropic finding), INTERPRETATION (applicability to research reports)

## Evaluation Frameworks Comparison

| Framework | What it does | Strengths | Weaknesses | Atlas relevance |
|-----------|-------------|-----------|------------|-----------------|
| Ragas | RAG evaluation (faithfulness, answer relevance, context precision) | Open-source, LLM-as-judge based, metrics for retrieval | RAG-focused, not general research reports | Medium |
| LangSmith | Tracing, evaluation, dataset management (LangChain) | Integrated with LangChain/LangGraph, production tracing | LangChain ecosystem, paid tiers | Medium-High |
| TruLens | LLM app evaluation and feedback | Open-source, feedback functions, app-centric | Smaller community | Medium |
| Custom LLM-as-judge | Rubric-based judge prompts | Full control, tailored to research reports | Must build and validate rubric | High |

## Research-Report Quality Metrics

| Metric | Description | Evaluation method |
|--------|-------------|-------------------|
| Accuracy | Claims supported by sources | Source verification + LLM-as-judge |
| Completeness | All research questions addressed | Checklist + LLM-as-judge |
| Source quality | Tier 1/2/3 sources cited | Source registry audit |
| Synthesis | Findings combined coherently | LLM-as-judge |
| Citation correctness | Links and dates present and valid | Link checking + manual audit |
| FACT/INTERP/HYPOTH/PROPOSAL labeling | Claims properly classified | Manual audit + LLM-as-judge |

## Cost Analysis of Automated Evaluation

LLM-as-judge adds token cost on top of research generation. Cost scales with: number of reports, report length, judge model capability, and number of rubric dimensions. For cycle 2 (5 reports), cost is modest. At scale (many cycles/domains), it becomes significant.

**Classification:** INTERPRETATION (extrapolation)

## Human + Automated Evaluation Hybrid Model

Recommendation: Use LLM-as-judge for initial screening (accuracy, completeness, source-quality flags), then human manager review for final APPROVED / REVISION REQUIRED / REJECTED decision. This balances cost and quality: automation catches obvious issues; humans judge nuance.

**Classification:** PROPOSAL (Atlas project convention)

## Recommendation for Atlas

Use a hybrid model: custom LLM-as-judge rubrics tailored to research-report quality metrics, with human manager review as the final gate. Start with a lightweight custom judge (no heavy framework dependency) in cycle 2; consider Ragas/LangSmith/TruLens if evaluation volume grows.

## Sources
- Anthropic Engineering, multi-agent research system, 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
- Ragas documentation — https://docs.ragas.io (2026)
- LangSmith documentation — https://docs.smith.langchain.com (2026)
- TruLens documentation — https://trulens.org (2026)
