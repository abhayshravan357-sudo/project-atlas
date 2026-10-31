# Goals and Scope — Project Atlas

## Primary goals

| Goal | Description | Success criterion |
|------|-------------|-------------------|
| G-01 | Produce evidence-backed research across multiple domains | Each domain has a report with sources cited |
| G-02 | Compare technology and architecture alternatives | Comparison matrices with trade-offs documented |
| G-03 | Maintain a centralized technical knowledge base | docs/ contains structured, cross-referenced documentation |
| G-04 | Guide incremental implementation | Every implementation milestone has corresponding documentation |
| G-05 | Enable owner to understand and maintain the system | Owner can navigate docs and codebase without guessing |

## Out of scope

Atlas will NOT:
- Be a general-purpose LLM chatbot or research assistant for arbitrary topics
- Replace human decision-making; it informs decisions
- Be a production search engine or web crawler (it uses existing search/LLM APIs)
- Be a code generation tool that writes full applications autonomously
- Be a deployment or DevOps platform (it documents deployment but does not provide infrastructure)

## Success criteria

- All research cycle reports are source-cited and classified (FACT / INTERPRETATION / HYPOTHESIS / PROPOSAL)
- Technology stack is documented with rationale for every dependency
- Architecture diagrams match the actual codebase
- Every code change is accompanied by documentation updates
- The project can be understood, tested, and extended by reading docs/ and src/
