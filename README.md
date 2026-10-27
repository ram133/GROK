# GROK

**Personal AI Agent Toolkit**  
Ship real automations, research, and content systems in minutes.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

> A living demonstration of what happens when you treat AI as a serious engineering partner instead of a chat toy.

**Live repo:** https://github.com/ram133/GROK

---

## Why this exists

Most AI projects are demos.  
GROK is built to become a product people actually use — and eventually pay for.

- Immediate utility on day one
- Clean architecture that scales
- Explicit commercial path (open-source core → hosted Pro)
- No vaporware features

---

## What works today (v0.1.1)

| Capability              | Status | Notes                                      |
|-------------------------|--------|--------------------------------------------|
| Natural language agent  | ✅      | Structured, useful output                  |
| Research agent          | ✅      | High-signal briefs                         |
| Content agent           | ✅      | Posts, threads, emails                     |
| Planning agent          | ✅      | Realistic execution plans                  |
| Beautiful CLI           | ✅      | `grok "your task"`                         |
| Python API              | ✅      | Clean `Agent().run(...)`                   |
| Extensible tools layer  | ✅      | Ready for real tools                       |
| Local-first design      | ✅      | No forced cloud dependency                 |

---

## Quick Start

```bash
git clone https://github.com/ram133/GROK.git
cd GROK
pip install -e .

# Instant value
grok "Research the biggest opportunities in personal AI agents for 2026"
grok "Write a high-signal LinkedIn post about shipping with AI"
grok "Create a 7-day plan to turn an open-source tool into a paid product"
```

Python:

```python
from grok import Agent

agent = Agent()
result = agent.run("Give me a sharp one-page brief on local vs cloud AI agents")
print(result.output)
```

---

## Architecture

```
grok/
├── agents/           # Specialized agents (research, content, planning...)
├── core/             # Runner, result model, tools interface
├── cli/              # Typer + Rich CLI
├── examples/         # Ready-to-run demos
└── docs/             # Clear documentation
```

Design principles:
- Thin orchestration
- Strong structured output
- Easy to extend with real tools (web, files, APIs, memory)
- Local-first, cloud when it actually helps

---

## Commercial Roadmap

**Now (Open Source)**  
Free, useful, well-documented core.

**Next**  
- Persistent memory  
- Real tool calling (web, files, calendar, email)  
- Simple local web UI  
- Plugin system  

**Later (Revenue)**  
- Hosted version with authentication  
- Team workspaces  
- Agent marketplace  
- Priority support / custom agents  

The open-source version is the top of the funnel.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).  
Ideas, bug reports, and especially real use-cases are highly valued.

---

## Credits

Actively developed with **Grok** (xAI) as primary collaborator.  
This is **not** an official xAI project — it is a personal showcase of high-leverage collaboration with AI.

---

## License

MIT

---

**Star the repo** if you want to watch (and help) a real product get built in public.
