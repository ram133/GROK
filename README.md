# GROK

**Personal AI Agent Toolkit**  
Ship real automations, research, and content systems in minutes.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Live Site](https://img.shields.io/badge/Live_Site-ram133.github.io%2FGROK-22d3ee)](https://ram133.github.io/GROK/)
[![Free First](https://img.shields.io/badge/Prime_Directive-FREE-22d3ee)](docs/free-ai-resources.md)

> A living demonstration of what happens when you treat AI as a serious engineering partner instead of a chat toy.

**Live site:** https://ram133.github.io/GROK/  
**Repo:** https://github.com/ram133/GROK  
**Free AI resources:** [docs/free-ai-resources.md](docs/free-ai-resources.md)  
**Agent guidance:** [AGENTS.md](AGENTS.md)

**Prime directive: FREE.** Core value requires zero credit cards and zero paid subscriptions. Optional free-tier LLMs can be plugged in later and always fall back to the local engine.

---

## Why this exists

Most AI projects are demos.  
GROK is built to become a product people actually use — and eventually pay for.

- Immediate utility on day one (no keys required)
- Clean architecture that scales
- Explicit commercial path (open-source core → hosted Pro)
- No vaporware features
- Strict free-first design

---

## What works today (v0.1.3)

| Capability                    | Status | Notes                                      |
|-------------------------------|--------|--------------------------------------------|
| Natural language agent        | ✅      | Structured, useful output                  |
| Research / Content / Planning | ✅      | High-signal patterns                       |
| Beautiful CLI + Python API    | ✅      | `grok "task"` / `Agent().run(...)`         |
| Local tools                   | ✅      | echo, local_time, system_info, list_dir, calc, web_search stub |
| Optional free LLM backend     | ✅      | OpenAI-compatible (Groq, OpenRouter :free, Gemini free, Ollama…) — falls back to local |
| Free AI resources doc         | ✅      | Curated no-card list                       |
| AGENTS.md guidance            | ✅      | For humans and other agents                |

---

## Quick Start (zero keys)

```bash
git clone https://github.com/ram133/GROK.git
cd GROK
pip install -e .

grok "Research the biggest opportunities in personal AI agents for 2026"
grok "Write a high-signal LinkedIn post about shipping with AI"
grok "Create a 7-day plan to turn an open-source tool into a paid product"
grok "list tools"
grok "tool:calc 17*3+4"
```

Python:

```python
from grok import Agent

agent = Agent()
result = agent.run("Give me a sharp one-page brief on local vs cloud AI agents")
print(result.output)
print(result.metadata)  # shows mode: local-free or free-llm
```

---

## Optional free LLM (still FREE)

Any OpenAI-compatible free endpoint works:

```bash
export GROK_LLM_BASE_URL="https://api.groq.com/openai/v1"
export GROK_LLM_API_KEY="gsk_..."          # free Groq key
export GROK_LLM_MODEL="llama-3.3-70b-versatile"

grok "Write a short research brief on free LLM APIs in 2026"
```

If the variables are missing or the call fails, GROK silently uses the local engine. No credit card required.

See `examples/with_free_llm.py` and `docs/free-ai-resources.md`.

---

## Free AI Resources

See [docs/free-ai-resources.md](docs/free-ai-resources.md) for the latest curated list of no-card LLM APIs, free coding agents, and local options.

---

## Commercial Path

**Now (Open Source)**  
Free, useful, well-documented core. No credit card required for core value.

**Want it customized or extended live?**  
→ [services](https://github.com/ram133/services) — $1 per minute

---

## Contact & Support

| Method | Details |
|--------|---------|
| **Phone / Signal** | +1 (671) 685-9138 · +1 (671) 456-6963 |
| **Email** | 3659745@gmail.com · crh2123@icloud.com |
| **Website** | [ray.services](https://ray.services) |
| **PayPal** | crh2123@icloud.com |
| **Custom agents / consulting** | $1/min live sessions |

All payments go directly to Ray.

---

## Credits

Actively developed with **Grok** (xAI) as primary collaborator.  
This is **not** an official xAI project — it is a personal showcase of high-leverage collaboration with AI under a strict FREE prime directive.

**Star the repo** if you want to watch (and help) a real product get built in public.
