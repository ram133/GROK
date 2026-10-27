"""Core Agent runner — the heart of GROK."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from .tools import get_tool

console = Console()


class AgentResult(BaseModel):
    """Structured result from every agent run."""
    task: str
    output: str
    success: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)


class Agent:
    """
    Personal AI agent focused on producing useful, structured work product.

    Design goals for v0.1:
    - Immediately useful without external API keys
    - Clean extension points for real tools and memory
    - Consistent, high-signal output format
    """

    def __init__(self, name: str = "GROK"):
        self.name = name

    def run(self, task: str, *, verbose: bool = True) -> AgentResult:
        """Execute a natural-language task and return structured output."""
        if verbose:
            console.print(Panel(f"[bold cyan]{self.name}[/] received task", title="Agent", border_style="cyan"))
            console.print(f"[dim]{task}[/]\n")

        output = self._dispatch(task)

        result = AgentResult(
            task=task,
            output=output,
            success=True,
            metadata={
                "agent": self.name,
                "version": "0.1.1",
            },
        )

        if verbose:
            console.print(Panel(Markdown(output), title="Result", border_style="green"))

        return result

    def _dispatch(self, task: str) -> str:
        """Route the task to the most appropriate response pattern."""
        t = task.lower()

        if any(k in t for k in ["research", "trends", "analyze", "summary", "brief", "report"]):
            return self._research(task)
        if any(k in t for k in ["write", "post", "thread", "email", "content", "linkedin", "tweet"]):
            return self._content(task)
        if any(k in t for k in ["plan", "roadmap", "strategy", "schedule", "launch"]):
            return self._plan(task)
        if any(k in t for k in ["tool", "echo"]):
            return self._tool_demo(task)

        return self._default(task)

    def _research(self, task: str) -> str:
        return f"""## Research Brief

**Query**  
{task}

### Core Thesis
Personal AI agents are shifting from novelty chat interfaces to persistent systems that own recurring outcomes. The winners in 2026 will be the ones that combine reliability, memory, and tight tool use rather than pure model size.

### Key Points
1. **Outcome ownership beats conversation** — users pay for finished work, not dialogue.
2. **Local-first + selective cloud** is the pragmatic architecture for most individuals and small teams.
3. **Thin orchestration + strong tools** is currently outperforming monolithic agent frameworks.
4. **Trust and auditability** are becoming purchase criteria, especially for business use.

### Implications
- Build for daily use, not demos.
- Instrument everything so users can see what the agent actually did.
- Start with one high-value recurring task and expand from there.

### Next Step
I can expand this into a full one-page brief, a competitor landscape table, or a concrete implementation plan. Tell me which one you want.
"""

    def _content(self, task: str) -> str:
        return f"""## Content Draft

**Request**  
{task}

### Hook
Most people still treat AI like a smarter search box.  
The ones pulling ahead treat it like a junior employee who never clocks out.

### Body
The difference is not the model.  
It is whether you give the system ownership of a recurring outcome and then measure the result.

When an agent owns the outcome, you stop prompting and start managing.

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
- Identify the smallest useful version that can be shipped
- List the three highest-leverage actions

### Phase 2 — Build (Days 2–5)
- Ship the smallest working version
- Get feedback from at least three real users
- Instrument basic usage signals

### Phase 3 — Tighten (Days 6–7)
- Fix the biggest friction points
- Document the happy path
- Decide whether to open-source, soft-launch, or both

### Success Criteria
You should be able to demonstrate clear value to a stranger in under two minutes by the end of the week.

**Want this turned into a day-by-day checklist with concrete outputs?**
"""

    def _tool_demo(self, task: str) -> str:
        tool = get_tool("echo")
        if tool:
            result = tool.run(text=task)
            return f"Tool layer is live.\n\nEcho tool returned:\n```\n{result}\n```"
        return "Tool layer is present but no matching tool was found."

    def _default(self, task: str) -> str:
        return f"""## Task Received

**{task}**

### Recommended Approach
1. Clarify the exact outcome you want
2. Break it into the smallest useful units of work
3. Execute the highest-leverage piece first
4. Measure the result and iterate

### Next Action
Tell me the single most important concrete result you need and I will produce it immediately.
"""
