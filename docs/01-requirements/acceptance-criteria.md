# Acceptance Criteria — Project Atlas

## For functional requirements

| ID | Acceptance criteria |
|----|---------------------|
| FR-01 | At least 3 research domains can be investigated in parallel; each domain produces a structured report in docs/research/<domain>/ |
| FR-02 | Each domain has its own Git branch and Git worktree; no two domains modify the same files simultaneously |
| FR-03 | Every factual claim in a report carries a source link and date, or is explicitly labeled HYPOTHESIS/PROPOSAL |
| FR-04 | Every report uses FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL labels consistently |
| FR-05 | Approved reports are synthesized into docs/knowledge-base/ with cross-references |
| FR-06 | docs/02-technology/technology-stack.md lists every dependency with purpose, version, and status |
| FR-07 | docs/09-management/decisions.md contains a record for each significant decision with reasoning, alternatives, and evidence |
| FR-08 | Each report passes an LLM-as-judge evaluation (score ≥ 0.75) before human manager review |
| FR-09 | For every code change, the relevant documentation file(s) are updated in the same commit |
| FR-10 | README.md contains setup and execution instructions for the development environment |

## For non-functional requirements

| ID | Acceptance criteria |
|----|---------------------|
| NFR-U-01 | Glossary (docs/00-overview/glossary.md) defines all technical terms used in documentation |
| NFR-U-02 | Every major component in src/ has a corresponding page in docs/04-implementation/module-documentation.md |
| NFR-M-01 | Code modules have clear boundaries; no circular dependencies between core modules |
| NFR-M-02 | Every package in libraries-and-packages.md has a "Why selected" rationale |
| NFR-T-01 | Every implemented feature has at least one test case |
| NFR-S-01 | Repository contains no committed API keys, secrets, or credentials |
| NFR-S-02 | Agent work is confined to assigned worktrees; no agent writes outside its directory |
| NFR-P-02 | Token cost estimates are documented for small, medium, and large research cycles |

## Documentation consistency checks

- [ ] Every source code change has a corresponding documentation update
- [ ] Every architecture change has an updated Mermaid diagram
- [ ] Every new dependency has an entry in libraries-and-packages.md
- [ ] Every decision has an entry in decisions.md
