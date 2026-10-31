# Alternatives — Project Atlas

## LangGraph alternatives

| Feature | LangGraph (selected) | Google ADK | AutoGen |
|---------|---------------------|------------|---------|
| Orchestration model | Graph-based with cycles | Sequential / coordinator / hierarchical | Conversation-driven |
| Persistence | Checkpoints (native) | session.state | Conversation history |
| Human-in-the-loop | Native interrupts | Not native | Limited |
| Ecosystem | LangChain | Google models | Microsoft / Semantic Kernel |
| Selected for Atlas? | Yes | Secondary | No |

## Python alternatives

| Feature | Python (selected) | TypeScript | Go | Rust |
|---------|------------------|------------|----|------|
| Agent library support | Dominant | Growing | Limited | Very limited |
| LLM provider SDKs | Python-native | Available | Limited | Limited |
| Ecosystem maturity | High | Medium | Medium | Low |
| Selected for Atlas? | Yes | Secondary | No | No |

## A2A decision

A2A (Agent-to-Agent protocol) was considered but deferred. The manager-centric orchestrator-worker model already handles coordination between agents through the manager. A2A becomes relevant only if Atlas moves to decentralized peer-to-peer orchestration, which is not in the initial scope.

## Status: Alternatives documented and rejected/deferred with reasoning
