# GROK Architecture

## Goals

- Useful on day one with zero external API keys (**FREE** prime directive)
- Clean extension points for real tools, memory, and multi-agent systems
- Clear separation between orchestration and capabilities
- Local-first by default; optional free-tier cloud is additive only

## Core Components

### Agent
The public entry point. Accepts a natural-language task and returns an `AgentResult`.
Default: high-signal local patterns. When `GROK_LLM_*` env vars are set, an optional free OpenAI-compatible LLM is tried first and falls back to local on any failure.

### AgentResult
Structured Pydantic model containing the original task, the output, success flag, and metadata (includes `mode`: `local-free` or `free-llm`).

### LLM Adapter (`grok/core/llm.py`)
Optional. Reads three env vars. Never required. Silent failure → local engine.

### Tools Layer
Thin interface (`Tool` base class + registry). Currently includes:

- `echo`
- `local_time`
- `system_info`
- `list_dir`
- `calc`
- `web_search` (stub + guidance for free providers)

Register new free tools in `AVAILABLE_TOOLS`.

### CLI
Typer + Rich. Designed to feel fast and professional.

## Extension Path

1. Add real tools by subclassing `Tool` and registering them
2. Point the free LLM adapter at any OpenAI-compatible free endpoint
3. Add memory by injecting a memory backend into `Agent`
4. Add multi-agent by composing multiple `Agent` instances with a coordinator
5. Keep the web UI calling the same `Agent.run()` interface

## Design Decisions

- Prefer structured output over free-form chat
- Keep the public API extremely stable even while internals evolve
- Optimize for the case where a single high-value recurring task is automated first
- Never make paid services a requirement for core value
