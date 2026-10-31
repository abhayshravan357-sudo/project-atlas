# Development Roadmap — Project Atlas

## Four Parallel Objectives

Project Atlas is guided by four parallel objectives:

| Objective | Description | Status |
|-----------|-------------|--------|
| O-01 | Build Project Atlas — a genuinely useful, functional multi-agent CLI orchestration tool | In Progress |
| O-02 | Build the engineering knowledge base — document every technology, dependency, decision, implementation and testing process | In Progress |
| O-03 | Grow GitHub contributions — regular, meaningful contributions through implementation, testing, documentation, reviews and issue resolution | In Progress |
| O-04 | Build the engineering portfolio — demonstrate Python, Git, testing, architecture, AI-agent orchestration and technical decision-making | In Progress |

## Phase 1 — Project Understanding (Complete)

- Repository audited: no source code, only research documentation
- Research cycles 1-3 completed and merged into main
- Project purpose: multi-agent research & exploration orchestrator using git worktrees for agent isolation

## Phase 2 — Documentation Foundation (Complete)

- Documentation structure established (00-overview through 09-management)
- Project vision, problem definition, goals, scope, features defined
- Functional and non-functional requirements defined
- User stories and acceptance criteria defined
- Technology stack documented and justified (Python, LangGraph, MCP, Git worktrees)

## Phase 3 — Architecture & Technical Decisions (Complete)

- System architecture documented (system, component, backend, data, API, frontend)
- Component diagram, data flow, state schema defined
- Architectural decisions recorded (D-001 through D-007)

## Phase 4 — Initial Implementation (Complete)

- Working development environment (pyproject.toml, pytest, coverage)
- Clear application entry point (`python -m atlas.cli`)
- Core orchestrator (plan → delegate → investigate → report → review → synthesize → commit → reassess)
- Basic integration between components (orchestrator → worktree manager → MCP servers)
- Initial tests (33 tests, all passing)
- Understandable code organization (src/atlas/ package)

## Phase 5 — Incremental Development (Complete)

- CLI interface: run-cycle, status, review, commit commands
- Test strategy, test cases, validation results documented
- MCP filesystem + git servers (stdio JSON-RPC, worktree-scoped, read-only git)
- Git integration tests using real temporary repositories and worktrees
- Quality audit: failure-path, CLI integration, MCP integration tests

## Phase 6 — Validation & Improvement (In Progress)

### Phase 6.1 — Validation Foundation (Complete)
- CI pipeline: `.github/workflows/ci.yml` (test + lint on push/PR, Python 3.10-3.12 matrix)
- Coverage reporting: `pyproject.toml` `[tool.coverage.*]` with `fail-under=80%`
- Git integration tests: `tests/test_git_integration.py` (12 tests)
- Quality audit tests: `tests/test_quality_audit.py` (9 tests)
- 33 tests pass; coverage 83.71% (>80% threshold)

### Phase 6.2 — Real Agent Delegation Investigation (In Progress)
- Subagent delegation confirmed working via `task` tool (file read and file write both executed successfully)
- Earlier aborts were transient, not a capability limitation
- Ready to delegate Phase 6.3+ assignments to independent subagents

### Phase 6.3 — LLM-as-Judge Review Gate (Planned)
- Define evaluation rubric
- Evaluate evidence, correctness, completeness, source quality, task compliance
- Human approval for consequential changes

### Phase 6.4 — Architecture Commitment (Planned)
- Evaluate implementation against requirements
- Identify unresolved technical risks
- Go / no-go decision on full implementation

## Contribution & Portfolio Tracking

See `docs/09-management/contribution-register.md` for the contribution register and `docs/09-management/agent-dashboard.md` for the contribution dashboard.

## Next Immediate Steps

1. Phase 6.2 — Investigate real agent delegation (why `task` aborts on real assignments)
2. Phase 6.3 — Implement LLM-as-judge review gate
3. Phase 6.4 — Architecture commitment / go-no-go decision
4. Continue Phase 5-style incremental feature development with tests and documentation
5. Push to GitHub (owner authorization required) to begin public contribution tracking
