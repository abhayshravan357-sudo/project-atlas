# Functional Requirements — Project Atlas

## Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-01 | The system shall coordinate research across multiple independent domains | High | At least 3 domains can be researched in parallel; each produces a report |
| FR-02 | Each research agent shall work in an isolated Git worktree on its own branch | High | Each domain has its own branch and worktree; no file conflicts |
| FR-03 | Research reports shall include source citations with links and dates | High | Every factual claim carries a source or is labeled HYPOTHESIS/PROPOSAL |
| FR-04 | Claims shall be classified as FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL | High | Every report uses the classification standard consistently |
| FR-05 | Approved research shall be synthesized into a centralized knowledge base | High | docs/knowledge-base/ contains synthesized findings from approved reports |
| FR-06 | Technology stack shall be documented with rationale for every dependency | High | docs/02-technology/ contains a technology-stack.md and per-technology explanations |
| FR-07 | Architecture decisions shall be recorded with reasoning and alternatives | High | docs/09-management/decisions.md contains decision records |
| FR-08 | Research-report quality shall be evaluated before integration | Medium | LLM-as-judge rubric applied; human manager gives final APPROVED / REVISED / REJECTED |
| FR-09 | Documentation shall be updated whenever implementation changes | Medium | For each code change, relevant docs/ files are updated |
| FR-10 | The project shall have a working development environment | Medium | README.md documents setup and execution steps |

## Non-functional requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-01 | Documentation shall be beginner-friendly without losing technical depth | High |
| NFR-02 | Every technology choice shall have a documented rationale | High |
| NFR-03 | Architecture diagrams shall match the actual codebase | High |
| NFR-04 | The system shall be maintainable and extensible | High |
| NFR-05 | Research results shall be reproducible from documented sources | Medium |
| NFR-06 | No unnecessary dependencies shall be added | Medium |
