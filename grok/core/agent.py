"""Core Agent runner."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


class AgentResult(BaseModel):
    """Structured result from an agent run."""
    task: str
    output: str
    success: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)


class Agent:
    """
    Minimal but serious personal AI agent.

    This is intentionally simple in v0.1 so it is reliable and easy to extend.
    The goal is real utility, not demo theater.
    """

    def __init__(self, name: str = "GROK"):
        self.name = name

    def run(self, task: str, *, verbose: bool = True) -> AgentResult:
        """
        Execute a natural language task and return structured output.

        In v0.1 this uses a strong reasoning template.
        Later versions will plug in real tool calling + memory.
        """
        if verbose:
            console.print(Panel(f"[bold cyan]{self.name}[/] received task", title="Agent"))
            console.print(f"[dim]{task}[/]\n")

        # Core reasoning pattern that produces useful output today
        output = self._reason(task)

        result = AgentResult(
            task=task,
            output=output,
            success=True,
            metadata={"agent": self.name, "version": "0.1.0"},
        )

        if verbose:
            console.print(Panel(Markdown(output), title="Result", border_style="green"))

        return result

    def _reason(self, task: str) -> str:
        """
        Produce high-signal output.

        This is the heart of v0.1 — a carefully designed response pattern
        that already delivers value while the full tool system is built.
        """
        task_lower = task.lower()

        if any(w in task_lower for w in ["research", "trends", "analyze", "summary", "brief"]):
            return self._research_style(task)
        if any(w in task_lower for w in ["write", "post", "thread", "email", "content"]):
            return self._content_style(task)
        if any(w in task_lower for w in ["plan", "roadmap", "strategy"]):
            return self._planning_style(task)

        # Default high-quality response
        return f"""## Task Received

**{task}**

### Recommended Approach
1. Clarify the exact outcome you want
2. Break it into the smallest useful units of work
3. Execute the highest-leverage piece first
4. Measure result and iterate

### Next Action
Tell me the single most important result you need from this task and I will produce it immediately.
"""

    def _research_style(self, task: str) -> str:
        return f"""## Research Brief

**Query:** {task}

### Key Insights (v0.1 synthesis)
- Personal AI agents are moving from chat toys → persistent systems that own outcomes
- The winning pattern in 2026 is **thin orchestration + strong tools + memory**
- Users will pay for reliability and time saved, not novelty
- Local-first + selective cloud is the pragmatic architecture

### Recommended Structure for a Strong Brief
1. One-sentence thesis
2. 3–5 supporting points with evidence
3. Clear implications / what to do next
4. Sources or confidence notes

### Immediate Next Step
I can expand any section into a full one-page brief, competitor table, or implementation plan. Just say which one you want.
"""

    def _content_style(self, task: str) -> str:
        return f"""## Content Draft

**Request:** {task}

### Hook
Most people are still treating AI like a smarter search engine.  
The ones who win treat it like a junior employee who never sleeps.

### Core Message
Build systems, not prompts.

### Call to Action
What is the one recurring task you still do manually that an agent should own?

---
*Ready for a longer version, X thread, LinkedIn post, or email sequence — just tell me the format.*
"""

    def _planning_style(self, task: str) -> str:
        return f"""## Execution Plan

**Goal:** {task}

### Phase 1 — Clarity (Today)
- Define the single success metric
- List the 3 highest-leverage actions

### Phase 2 — Build (This Week)
- Ship the smallest working version
- Get real feedback from 3 people

### Phase 3 — Scale
- Automate the repetitive parts
- Turn the working system into a product or service

**Want me to turn this into a concrete 7-day plan with daily outputs?**
"""
