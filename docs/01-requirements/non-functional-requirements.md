# Non-Functional Requirements — Project Atlas

## Understandability

- **NFR-U-01**: Documentation shall use plain language where possible, with technical terms defined in the glossary.
- **NFR-U-02**: Every major component shall have a module documentation page explaining its purpose, inputs, outputs, and dependencies.
- **NFR-U-03**: Architecture diagrams shall use Mermaid and be kept in sync with code changes.

## Maintainability

- **NFR-M-01**: Code shall be organized into clearly separated modules with single responsibilities.
- **NFR-M-02**: Every dependency shall have a documented purpose and selection rationale.
- **NFR-M-03**: Architectural decisions shall be recorded in decisions.md with context, alternatives, and evidence.

## Modularity

- **NFR-Mod-01**: Components shall have well-defined interfaces.
- **NFR-Mod-02**: No component shall depend on internal implementation details of another component.

## Testability

- **NFR-T-01**: Every completed milestone shall have corresponding tests.
- **NFR-T-02**: Test cases shall be documented in docs/06-testing/.

## Reproducibility

- **NFR-R-01**: Research results shall be traceable to cited sources.
- **NFR-R-02**: The development environment shall be reproducible from documented setup steps.

## Security

- **NFR-S-01**: No secrets or API keys shall be stored in the repository.
- **NFR-S-02**: Agents shall operate with least-privilege access to the filesystem (worktree-scoped).

## Performance

- **NFR-P-01**: Research cycles shall complete in a reasonable wall-clock time (agent-dependent).
- **NFR-P-02**: Token cost shall be tracked and reported per cycle where measurable.

## Usability

- **NFR-UX-01**: The project shall have a clear entry point (README.md and docs/00-overview/).
- **NFR-UX-02**: The documentation structure shall be predictable (numbered sections 00-09).
