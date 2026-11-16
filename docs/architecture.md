# GROK Architecture

## Goals

- Useful on day one with zero external API keys (**FREE** prime directive)
- Clean extension points for real tools, memory, and multi-agent systems
- Clear separation between orchestration and capabilities
- Local-first by default; optional free-tier cloud is additive only

## Core Components

### Agent
The public entry point. Accepts a natural-language task and returns an `AgentResult`.
Currently uses high-signal local patterns. Designed so an optional free LLM backend can be swapped in later without changing the public API.

### AgentResult
Structured Pydantic model containing the original task, the output, success flag, and metadata.

### Tools Layer
Thin interface (`Tool` base class + registry). Currently includes:

- `echo` — testing
- `local_time` — current local time (fully free)
- `system_info` — basic platform info (fully free)

This is where web search, file operations, calendar, email, and other capabilities will live. Prefer free / local implementations first.

### CLI
Typer + Rich. Designed to feel fast and professional.

## Extension Path

1. Add real tools by subclassing `Tool` and registering them
2. Add optional free LLM backends via environment variables (OpenAI-compatible)
3. Add memory by injecting a memory backend into `Agent`
4. Add multi-agent by composing multiple `Agent` instances with a coordinator
5. Keep the web UI calling the same `Agent.run()` interface

## Design Decisions

- Prefer structured output over free-form chat
- Keep the public API extremely stable even while internals evolve
- Optimize for the case where a single high-value recurring task is automated first
- Never make paid services a requirement for core value
