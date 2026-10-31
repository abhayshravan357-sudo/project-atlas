# Agent Assignment — Fundamentals Investigator (Agent A)

## Agent Identity
- ID: A
- Name: Agent A
- Role: Fundamentals Investigator
- Branch: research/fundamentals
- Worktree: /tmp/atlast-wt/fundamentals

## Research Objective
Investigate basic concepts, terminology, prerequisites, learning paths, and advanced foundations relevant to a multi-agent research orchestrator like Project Atlas. Produce a structured, evidence-backed research report. Do NOT decide direction, do NOT write code, do NOT commit to Git.

## Scope
Core multi-agent concepts, orchestrator/worker definitions, prerequisites (git/worktrees, LLM APIs, orchestration frameworks, CLI), research-cycle phases, advanced foundations (communication, state, memory, evaluation, tool use, human-in-the-loop), and what Atlas's owner must understand before choosing a direction.

## Questions to Investigate
1. What is a multi-agent system (MAS)? What is an orchestrator / orchestrator-worker pattern? Define core concepts.
2. Key terminology with definitions: orchestrator, worker/subagent, agent, task, delegation, worktree, branch, synthesis, knowledge base, FACT/INTERPRETATION/HYPOTHESIS/PROPOSAL.
3. Prerequisites for building/running an agent research orchestrator: git & worktrees, LLM APIs/providers, orchestration frameworks, CLI tooling, version control concepts.
4. What does a research cycle look like? (plan → delegate → investigate → report → review → synthesize → commit → reassess). Describe each phase.
5. Advanced foundations: agent communication protocols, shared state/session state, memory (short/long-term), evaluation (LLM-as-judge), tool use, human-in-the-loop.
6. What concepts must Atlas's owner understand before choosing a direction?

## Expected Depth
Broad but structured. Define each term, explain how it works, why it matters to Atlas, where it is used. Target ~800-1200 words equivalent.

## Research Methodology
Use official documentation, reputable engineering blogs, academic survey papers, framework documentation. Distinguish FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL. Cite sources with links and publication dates where available. Do not fabricate citations, statistics, features, or capabilities. When evidence is insufficient, state that explicitly.

## Required Output Files
Return report as Markdown covering:
- # Agent A Report — Fundamentals
- Core Concepts (multi-agent system, orchestrator, worker)
- Glossary / Terminology table (term, definition, relevance to Atlas, classification FACT/INTERP/HYPOTH/PROPOSAL)
- Prerequisites (git/worktrees, LLM APIs, frameworks, CLI; each with what/why/requirements)
- Research Cycle phases (plan/delegate/investigate/report/review/synthesize/commit/reassess)
- Advanced Foundations (communication, state, memory, evaluation, tool use, human-in-the-loop)
- Open Questions / What remains unknown
- Sources (links + dates)

## Evidence Requirements
Every important claim must carry a source link and date, or be labeled HYPOTHESIS/INTERPRETATION.

## Restrictions
- No application code.
- No Git commits/merges/pushes.
- Do not modify main branch.
- Do not write files to disk (return report in response); the Main Agent will place reports.
- Do not assume a single architecture for Atlas.

## Completion Criteria
Report returned covering all 6 question areas, with glossary table, source list, and clear FACT/INTERP/HYPOTH/PROPOSAL labeling.
