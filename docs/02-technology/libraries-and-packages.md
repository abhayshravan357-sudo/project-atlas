# Libraries and Packages — Project Atlas

| Package | Purpose | Version | Status | Why needed |
|---------|---------|---------|--------|------------|
| langgraph | Agent orchestration framework | Latest | Proposed | Core orchestration (plan→delegate→...→reassess cycle) |
| langchain-core | LangChain core abstractions | Latest | Proposed | Dependency of LangGraph; prompt/output parsing |
| anthropic | Anthropic Claude API client | Latest | Proposed | LLM provider for agents |
| pytest | Testing framework | Latest | Proposed | Unit and integration tests |
| python-dotenv | Environment variable loading | Latest | Proposed | Load API keys from .env (not committed) |

## Notes
- No packages are installed yet (no source code exists).
- All packages will be installed in a virtual environment.
- API keys will be stored in .env, never committed to Git.
- Minimal dependency set: only what is needed for the orchestrator, tests, and CLI.

## Status: All proposed
