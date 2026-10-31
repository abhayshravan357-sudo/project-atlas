# Frameworks — Project Atlas

## LangGraph

### 1. What is it?
LangGraph is a graph-based orchestration framework for LLM agents, built on LangChain. Agents are nodes in a StateGraph; edges define control flow including cycles (loops), conditional routing, and persistence via checkpoints.

### 2. Why does our project need it?
Project Atlas needs to coordinate multiple agents through a research cycle (plan → delegate → investigate → report → review → synthesize → commit → reassess). LangGraph's graph model with cycles maps directly to this cycle, and its checkpoints support human-in-the-loop review at the review node.

### 3. Where is it used?
src/orchestrator/ — the LangGraph StateGraph defining the research cycle nodes and edges.

### 4. How does it work?
Define a StateGraph with a shared state schema. Add nodes (Python functions) and edges (control flow). Compile into a runnable. LangGraph manages state passing, persistence (checkpoints), and streaming. The `interrupt()` function enables human-in-the-loop review before committing.

### 5. How does it communicate with other components?
LangGraph nodes call MCP tools for agent capabilities. Nodes read/write shared state. The review node interrupts and waits for manager approval.

### 6. Why did we select it?
- Graph model with cycles fits the research cycle (reassess loops back to plan)
- Native persistence/checkpoints for resuming long-running cycles
- Native human-in-the-loop interrupts for the manager review gate
- Python-native, aligns with our language choice
- Cycle 2 comparison ranked it highest for Atlas suitability

### 7. What alternatives exist?
- **Google ADK**: Sequential, coordinator/dispatcher, hierarchical patterns; session.state management; good but Google-centric
- **AutoGen / Microsoft Agent Framework**: Conversation-driven; ecosystem convergence with Semantic Kernel adds uncertainty
- **CrewAI**: Role-based agents; simpler but less flexible for complex graphs

### 8. Advantages
- Fine-grained control over orchestration
- Cycles and conditional routing
- Persistence and time-travel debugging
- Native human-in-the-loop interrupts
- Active LangChain ecosystem

### 9. Disadvantages
- Steep learning curve
- Python-centric
- Operational complexity (managing checkpoints, state)

### 10. What should the project owner learn?
- StateGraph concepts (nodes, edges, state)
- Checkpoints and persistence
- Human-in-the-loop interrupts
- Streaming and state inspection

### 11. Practical example
```python
from langgraph.graph import StateGraph, END

builder = StateGraph(ResearchState)
builder.add_node("plan", plan_node)
builder.add_node("review", review_node)
builder.add_edge("plan", "review")
builder.add_conditional_edges("review", should_continue)
graph = builder.compile()
```

### 12. References
- LangGraph documentation: https://langchain-ai.github.io/langgraph/
- LangChain: https://langchain.com/

## Status: Proposed (not yet implemented — no source code exists yet)
