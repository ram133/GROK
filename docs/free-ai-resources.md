# Free AI Resources (Updated Nov 2026)

**Prime directive of this repository: everything stays FREE.**

This list prioritizes no-credit-card, no-paid-subscription options that actually deliver useful capability today.

## Free LLM APIs (OpenAI-compatible preferred)

| Provider | Free models / notes | Card required? | Notes |
|----------|---------------------|----------------|-------|
| **Google AI Studio (Gemini)** | Gemini Flash / Flash-Lite family, embeddings, some Pro limited | No | Strong free tier. Get key at aistudio.google.com |
| **Groq** | Open-weight models (Qwen, GPT-OSS variants), Whisper | No (phone for signup) | Extremely fast. api.groq.com |
| **OpenRouter** | Models ending in `:free` | No | One key, many free models. Rotating list. 20 RPM / 50 RPD base |
| **Cloudflare Workers AI** | Multiple models | No | 10k Neurons/day free |
| **NVIDIA NIM / build.nvidia.com** | Selected open models marked Free Endpoint | No | Good for open weights |

**How to use in GROK** (coming / experimental):

```bash
export GROK_LLM_BASE_URL="https://api.groq.com/openai/v1"
export GROK_LLM_API_KEY="gsk_..."
export GROK_LLM_MODEL="llama-3.3-70b-versatile"  # or any free model
grok "your task"
```

If no key is set, GROK falls back to its high-quality local rule engine (always free, always works).

## Free Coding Agents & Tools

- **Aider** — Terminal pair-programming agent (Apache 2.0). Bring your own free model key or local.
- **Cline / Roo Code** — VS Code agent extensions (open source). BYOK or free providers.
- **OpenCode** — Terminal agent with free model routes.
- **Continue.dev** — Open-source IDE agent.
- **Ollama** + local models — Fully offline, zero cost after download.
- **GitHub Copilot Free** — Limited completions + chat (no card for basic free tier in many regions).
- **Cursor Hobby** — Free plan with limits.
- **Google Antigravity** — Free individual agentic IDE plan (weekly limits).

## Free Chat & Research

- Google Gemini (web + app) — Generous free tier including Deep Research features on free.
- ChatGPT Free — Unlimited everyday text.
- Perplexity Free — Unlimited basic search + limited Pro.
- Claude Free — Strong reasoning, usage windows.
- DeepSeek, Qwen, Kimi free web interfaces.

## Local / Fully Offline

- Ollama
- llama.cpp
- LM Studio
- Open WebUI / LibreChat (self-hosted frontends)

## Principles for this repo

1. Never require a paid subscription or credit card to get core value.
2. Optional free-tier cloud is fine; local/rule-based must always work.
3. Document limits honestly.
4. Prefer OpenAI-compatible endpoints so one adapter covers many providers.

Last updated: 2026-11-16
