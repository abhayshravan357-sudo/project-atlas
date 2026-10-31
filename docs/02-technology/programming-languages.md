# Programming Languages — Project Atlas

## Python

### 1. What is it?
Python is a high-level, interpreted, general-purpose programming language with a large standard library and a dominant ecosystem for AI/ML and agent development.

### 2. Why does our project need it?
Project Atlas is an LLM-based agent orchestrator. The dominant agent frameworks (LangGraph, LangChain, AutoGen, Google ADK) are Python-first or Python-only. Python is required to use these frameworks and their LLM integrations.

### 3. Where is it used?
All implementation code in src/ (orchestrator, workers, CLI, MCP client integration, tests).

### 4. How does it work?
Python source files are interpreted at runtime. Agents are implemented as Python functions/nodes in a LangGraph StateGraph. LLM calls are made via provider SDKs (Anthropic, OpenAI, etc.).

### 5. How does it communicate with other components?
Python components import each other as modules. LangGraph nodes pass state objects between nodes. MCP clients call MCP servers over stdio or HTTP.

### 6. Why did we select it?
- Dominant LLM/agent library support (LangGraph, LangChain, CrewAI, AutoGen are Python-first)
- LLM provider SDKs (Anthropic, OpenAI, Google) are Python-native
- Large community, extensive documentation, easy hiring/onboarding
- Cycle 2 technology comparison confirmed Python as high suitability

### 7. What alternatives exist?
- **TypeScript/JavaScript**: Growing agent ecosystem, good for CLI/web frontends, but LLM agent library support lags Python
- **Go**: Excellent concurrency and deployment, but immature agent/LLM library ecosystem
- **Rust**: Strong safety and performance, but very immature agent ecosystem

### 8. Advantages
- Best agent/LLM library support
- Rich ecosystem of LLM provider SDKs
- Easy to read and maintain (aligns with Project Atlas understandability goal)
- Large talent pool

### 9. Disadvantages
- GIL limits true parallelism in threads (mitigated by async and multiprocessing)
- Slower than compiled languages (not a bottleneck for LLM-bound agent work)

### 10. What should the project owner learn?
- Python syntax, data structures, functions, classes
- async/await for concurrent I/O
- Virtual environments (venv/conda) and dependency management (pip)
- Basic testing with pytest

### 11. Practical example
```python
# Example: A LangGraph node that delegates research to a worker
def plan_node(state: ResearchState) -> ResearchState:
    domains = decompose_objective(state["objective"])
    return {"domains": domains, "phase": "delegate"}
```

### 12. References
- Python documentation: https://docs.python.org/3/
- LangGraph Python docs: https://langchain-ai.github.io/langgraph/

## Status: Proposed (not yet implemented — no source code exists yet)
