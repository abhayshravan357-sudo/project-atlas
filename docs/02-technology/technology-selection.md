# Technology Selection — Project Atlas

## Decision rationale

| Technology | Selected | Reasoning | Trade-offs |
|------------|----------|-----------|------------|
| Python | Yes | Dominant agent/LLM library support; LangGraph is Python-first; LLM provider SDKs are Python-native | GIL limits thread parallelism; slower than compiled languages (not a bottleneck for LLM-bound work) |
| LangGraph | Yes | Graph model with cycles fits research cycle; native checkpoints and human-in-the-loop interrupts; Python-native | Steep learning curve; operational complexity |
| MCP | Yes (proposed) | Standardized agent-to-tool communication; growing server ecosystem | Early stage; client support uneven |
| A2A | No (deferred) | Very early; few implementations; manager-centric model already handles coordination | Not needed for initial scope |
| pytest | Yes | Standard Python testing; widely understood | None significant |
| Click/Typer | Optional | CLI interface for future use | Not needed yet |

## Alignment with Cycle 2/3 findings
- Cycle 2 technology comparison: LangGraph highest suitability for Atlas
- Cycle 2 integration protocols: MCP for tool access; defer A2A
- Cycle 3 cost validation: cost feasible at small/medium scale
- Cycle 3 prototype design: LangGraph orchestrator-worker graph with review gate

## Status: All selections documented
