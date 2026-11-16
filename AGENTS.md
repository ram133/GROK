# AGENTS.md — GROK Guidance

**Prime directive: FREE.**

This file is for humans and for other agents that may work on this repository.

## Core rules

1. Never make a paid service or credit card required for core value.
2. Local / rule-based behavior must always work with zero configuration.
3. Optional free-tier LLM backends are welcome (OpenAI-compatible). They must fall back cleanly.
4. Prefer structured, high-signal output over free-form chat.
5. Keep the public `Agent.run(task)` API stable.

## How the agent currently works

- Default mode: high-quality local patterns (research / content / plan + tools).
- Optional mode: set three environment variables and any OpenAI-compatible free endpoint is used:
  - `GROK_LLM_BASE_URL`
  - `GROK_LLM_API_KEY`
  - `GROK_LLM_MODEL`
- Tools live in `grok/core/tools.py`. Register new free tools there.

## Adding a free tool

```python
class MyFreeTool(Tool):
    name = "my_tool"
    description = "Does something useful with no paid dependency."

    def run(self, **kwargs):
        ...

AVAILABLE_TOOLS["my_tool"] = MyFreeTool
```

## Adding / improving free LLM support

See `grok/core/llm.py`. Keep failures silent so the local engine always remains available.

## Preferred free backends (as of Nov 2026)

- Groq free tier
- OpenRouter models ending in `:free`
- Google AI Studio / Gemini free tier
- Local models via Ollama (point BASE_URL at localhost)

See `docs/free-ai-resources.md` for the full curated list.

## What “done” looks like for a change

- Works with zero keys.
- Documented in README or free-ai-resources if user-facing.
- Version bumped if public behavior changes.
- No secrets committed.
