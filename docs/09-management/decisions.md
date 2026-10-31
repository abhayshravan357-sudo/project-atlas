# Decisions — Project Atlas

Important architectural and technical decisions.

## D-001 | 2026-10-31 | Research-first workflow; no application code in cycle 1
**Reasoning:** Repository was empty; priority was knowledge base before implementation.
**Alternatives:** Implement a prototype first.
**Evidence:** Repository inspection (README placeholder, single commit).

## D-002 | 2026-10-31 | Seven initial research domains for cycle 1
**Reasoning:** Covers fundamentals through critical analysis; broad discovery.
**Alternatives:** Single deep dive on one technology.
**Evidence:** Project Atlas objective (explore many directions).

## D-003 | 2026-10-31 | Isolated Git worktrees per research domain
**Reasoning:** Keeps main clean; no file conflicts between agents; audit trail via git.
**Alternatives:** Multiple clones; single shared working dir.
**Evidence:** Git worktree inspection; branch isolation requirement.

## D-004 | 2026-10-31 | LangGraph as primary orchestration framework
**Reasoning:** Graph model with cycles, persistence, native human-in-the-loop interrupts maps to research cycle.
**Alternatives:** Google ADK (secondary), AutoGen (not recommended — ecosystem convergence).
**Evidence:** Agent I Report — Cycle 2 Technology Comparison.

## D-005 | 2026-10-31 | MCP for agent tool access; defer A2A
**Reasoning:** MCP is emerging with growing server ecosystem; A2A is very early with few implementations.
**Alternatives:** Adopt both / neither.
**Evidence:** Agent J Report — Cycle 2 Integration Protocols.

## D-006 | 2026-10-31 | Python as primary implementation language
**Reasoning:** Dominant LLM/agent library support; LangGraph is Python-centric.
**Alternatives:** TypeScript (secondary for CLI/tooling), Go/Rust (immature agent ecosystem).
**Evidence:** Agent B Report — Cycle 2 Technology Landscape.

## D-007 | 2026-10-31 | Git worktrees as agent isolation primitive
**Reasoning:** Strong filesystem isolation; each agent works on own branch; clean main.
**Alternatives:** Multiple clones, container per agent.
**Evidence:** Cycle 1-3 research; git worktree documentation.

## D-008 | 2026-10-31 | GitHub contribution growth as explicit secondary objective
**Reasoning:** The project should demonstrate consistent engineering growth on GitHub, not just build software. Contribution activity must emerge from meaningful engineering work — not empty commits.
**Alternatives:** Build silently without tracking contributions; manufacture activity with empty commits (rejected).
**Evidence:** Owner directive — contribution activity and quality are explicit parallel objectives alongside building the CLI tool and knowledge base.

## D-009 | 2026-10-31 | Independent AI subagent delegation is available via `task` tool
**Reasoning:** Two real work assignments were successfully executed by independent subagents (file reading and file creation). Earlier aborts were transient, not a capability limitation.
**Alternatives:** Manual-manager execution only (rejected — subagent delegation works).
**Evidence:** Two `task` tool calls returned successful results with verified file output.

## Pending Decisions

- Exact CLI command structure (to be decided by CLI Agent).
- Test framework selection (pytest vs alternatives — to be decided by QA Agent).
- MCP server implementation approach (stdio vs HTTP per server — to be decided by Integration Agent).
