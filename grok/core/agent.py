"""Core Agent runner — the heart of GROK.

Prime directive: FREE.
- Works with zero API keys (high-signal local patterns).
- Optional free-tier LLM backends via env vars (Groq / OpenRouter free / Gemini free etc.).
- Tools layer stays thin and local-first.
"""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from .tools import get_tool, list_tools
from .llm import call_llm, llm_available

console = Console()

SYSTEM_PROMPT = """You are GROK, a personal AI agent toolkit focused on high-signal, structured work product.
Prefer clear thesis → key points → next action format.
Be concise, practical, and free-first (no paid services required for core value).
Never invent facts you cannot support."""


class AgentResult(BaseModel):
    """Structured result from every agent run."""
    task: str
    output: str
    success: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)


class Agent:
    """
    Personal AI agent focused on producing useful, structured work product.

    Design goals:
    - Immediately useful without external API keys (FREE)
    - Clean extension points for real tools and optional free LLMs
    - Consistent, high-signal output format
    """

    def __init__(self, name: str = "GROK"):
        self.name = name

    def run(self, task: str, *, verbose: bool = True) -> AgentResult:
        """Execute a natural-language task and return structured output."""
        if verbose:
            console.print(Panel(f"[bold cyan]{self.name}[/] received task", title="Agent", border_style="cyan"))
            console.print(f"[dim]{task}[/]\n")

        mode = "local-free"
        output = self._dispatch(task)

        # Optional free LLM enhancement (never required)
        if llm_available() and not self._is_simple_tool_task(task):
            llm_out = call_llm(task, system=SYSTEM_PROMPT)
            if llm_out:
                output = llm_out
                mode = "free-llm"

        result = AgentResult(
            task=task,
            output=output,
            success=True,
            metadata={
                "agent": self.name,
                "version": "0.1.3",
                "mode": mode,
                "llm_configured": llm_available(),
            },
        )

        if verbose:
            console.print(Panel(Markdown(output), title="Result", border_style="green"))

        return result

    def _is_simple_tool_task(self, task: str) -> bool:
        t = task.lower().strip()
        return (
            t.startswith("tool:")
            or t.startswith("/tool ")
            or any(k in t for k in ["list tools", "what tools", "available tools", "local time", "system info"])
        )

    def _dispatch(self, task: str) -> str:
        """Route the task to the most appropriate response pattern."""
        t = task.lower().strip()

        # Explicit tool requests
        if t.startswith("tool:") or t.startswith("/tool "):
            return self._run_named_tool(t)
        if any(k in t for k in ["list tools", "what tools", "available tools"]):
            return self._list_tools()

        if any(k in t for k in ["research", "trends", "analyze", "summary", "brief", "report", "opportunities"]):
            return self._research(task)
        if any(k in t for k in ["write", "post", "thread", "email", "content", "linkedin", "tweet"]):
            return self._content(task)
        if any(k in t for k in ["plan", "roadmap", "strategy", "schedule", "launch", "7-day"]):
            return self._plan(task)
        if any(k in t for k in ["time", "date", "what time"]):
            tool = get_tool("local_time")
            if tool:
                return f"Current local time: **{tool.run()}**"
        if any(k in t for k in ["system", "python version", "platform"]):
            tool = get_tool("system_info")
            if tool:
                info = tool.run()
                return "## System Info\n\n" + "\n".join(f"- **{k}**: {v}" for k, v in info.items())
        if any(k in t for k in ["list dir", "list files", "ls "]):
            tool = get_tool("list_dir")
            if tool:
                items = tool.run()
                return "## Directory listing\n\n" + "\n".join(f"- {i}" for i in items)
        if t.startswith("calc ") or t.startswith("calculate "):
            expr = task.split(maxsplit=1)[1] if " " in task else ""
            tool = get_tool("calc")
            if tool:
                return f"**Calc** → `{tool.run(expression=expr)}`"

        return self._default(task)

    def _run_named_tool(self, task: str) -> str:
        parts = task.replace("tool:", "").replace("/tool", "").strip().split(maxsplit=1)
        name = parts[0] if parts else ""
        arg = parts[1] if len(parts) > 1 else ""
        tool = get_tool(name)
        if not tool:
            return f"Unknown tool `{name}`. Available tools:\n" + self._list_tools()
        try:
            if name == "echo":
                result = tool.run(text=arg)
            elif name == "list_dir":
                result = tool.run(path=arg or ".")
            elif name == "calc":
                result = tool.run(expression=arg)
            elif name == "web_search":
                result = tool.run(query=arg)
            else:
                result = tool.run()
            return f"**Tool `{name}` result**\n\n```\n{result}\n```"
        except Exception as e:
            return f"Tool `{name}` failed: {e}"

    def _list_tools(self) -> str:
        tools = list_tools()
        lines = ["## Available Tools (all free / local by default)\n"]
        for t in tools:
            lines.append(f"- **{t['name']}**: {t['description']}")
        lines.append("\nUsage: `tool:echo hello`, `tool:calc 2+2*10`, `tool:list_dir .`")
        lines.append("\nOptional free LLM: set GROK_LLM_BASE_URL + GROK_LLM_API_KEY + GROK_LLM_MODEL")
        return "\n".join(lines)

    def _research(self, task: str) -> str:
        return f"""## Research Brief

**Query**  
{task}

### Core Thesis
Personal AI agents are shifting from novelty chat interfaces to persistent systems that own recurring outcomes. The winners in 2026 will be the ones that combine reliability, memory, and tight tool use rather than pure model size.

### Key Points
1. **Outcome ownership beats conversation** — users pay for finished work, not dialogue.
2. **Local-first + selective free-tier cloud** is the pragmatic architecture for most individuals and small teams.
3. **Thin orchestration + strong tools** is currently outperforming monolithic agent frameworks.
4. **Trust and auditability** are becoming purchase criteria, especially for business use.
5. **Free tiers of strong models** (Gemini Flash, Groq open models, OpenRouter :free) make high-capability agents accessible without credit cards.

### Implications
- Build for daily use, not demos.
- Instrument everything so users can see what the agent actually did.
- Start with one high-value recurring task and expand from there.
- Prefer free or local backends by default.

### Next Step
I can expand this into a full one-page brief, a competitor landscape table, or a concrete implementation plan. Tell me which one you want.
"""

    def _content(self, task: str) -> str:
        return f"""## Content Draft

**Request**  
{task}

### Hook
Most people still treat AI like a smarter search box.  
The ones pulling ahead treat it like a junior employee who never clocks out — and they keep the core free.

### Body
The difference is not the model.  
It is whether you give the system ownership of a recurring outcome and then measure the result.

When an agent owns the outcome, you stop prompting and start managing.

GROK is built under a strict free-first rule: useful on day one with zero paid services, optional free-tier LLMs later.

### Close
What is the one task you still do manually every week that an agent should own instead?

---
*Ready for a longer version, X thread, LinkedIn post, email sequence, or landing-page copy — just specify the format and tone.*
"""

    def _plan(self, task: str) -> str:
        return f"""## Execution Plan

**Goal**  
{task}

### Phase 1 — Clarity (Day 1)
- Define the single success metric
- Identify the smallest useful version that can be shipped for free
- List the three highest-leverage actions

### Phase 2 — Build (Days 2–5)
- Ship the smallest working version (local-first)
- Get feedback from at least three real users
- Instrument basic usage signals
- Optionally plug in free LLM tiers if they improve quality

### Phase 3 — Tighten (Days 6–7)
- Fix the biggest friction points
- Document the happy path and the free constraints
- Decide whether to open-source more, soft-launch, or both

### Success Criteria
You should be able to demonstrate clear value to a stranger in under two minutes by the end of the week — without asking them for a credit card.

**Want this turned into a day-by-day checklist with concrete outputs?**
"""

    def _default(self, task: str) -> str:
        return f"""## Task Received

**{task}**

### Recommended Approach
1. Clarify the exact outcome you want
2. Break it into the smallest useful units of work
3. Execute the highest-leverage piece first (using free / local tools)
4. Measure the result and iterate

### Next Action
Tell me the single most important concrete result you need and I will produce it immediately.

(All core GROK capabilities remain free. Optional free LLM activates automatically when GROK_LLM_* env vars are set.)
"""
