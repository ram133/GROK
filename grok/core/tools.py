"""Tools interface for GROK agents.

Prime directive: FREE. The base layer requires zero paid services.
Optional free-tier LLM / search backends can be plugged in later.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Tool(ABC):
    """Base class for all tools."""

    name: str
    description: str

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Execute the tool."""
        ...


class EchoTool(Tool):
    """Simple tool used for testing the interface."""

    name = "echo"
    description = "Returns the input unchanged. Useful for testing."

    def run(self, text: str = "") -> str:
        return text


class LocalTimeTool(Tool):
    """Return current local time — fully free, no network."""

    name = "local_time"
    description = "Return the current local date and time."

    def run(self, **kwargs: Any) -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")


class SystemInfoTool(Tool):
    """Basic system info — free and local."""

    name = "system_info"
    description = "Return basic Python / platform information."

    def run(self, **kwargs: Any) -> dict[str, str]:
        import platform
        import sys
        return {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "machine": platform.machine(),
        }


class ListDirTool(Tool):
    """List files in a directory (local, free). Defaults to current dir."""

    name = "list_dir"
    description = "List files and folders in a path (default: current directory)."

    def run(self, path: str = ".") -> list[str]:
        p = Path(path).expanduser().resolve()
        if not p.exists():
            return [f"Path does not exist: {p}"]
        if not p.is_dir():
            return [f"Not a directory: {p}"]
        try:
            return sorted([f.name + ("/" if f.is_dir() else "") for f in p.iterdir()])[:80]
        except Exception as e:
            return [f"Error: {e}"]


class CalcTool(Tool):
    """Tiny safe calculator — free, no network."""

    name = "calc"
    description = "Evaluate a simple math expression (numbers and + - * / ** () only)."

    def run(self, expression: str = "") -> str:
        expr = expression.strip()
        if not expr:
            return "Provide an expression, e.g. 2 + 2 * 10"
        allowed = set("0123456789+-*/().% ** ")
        if not all(c in allowed for c in expr.replace("**", "")):
            return "Only basic arithmetic is allowed."
        try:
            # Restricted eval for simple math
            result = eval(expr, {"__builtins__": {}}, {})
            return str(result)
        except Exception as e:
            return f"Calc error: {e}"


class FreeSearchStubTool(Tool):
    """Placeholder for free web search. Documents how to plug a real free provider later."""

    name = "web_search"
    description = "Stub for free web search. Returns guidance until a free provider is configured."

    def run(self, query: str = "") -> str:
        return (
            f"Search stub for: {query}\n\n"
            "No free search backend is hard-wired yet (keeps the core zero-dependency).\n"
            "To add one later: implement a Tool that calls a free search API or "
            "a local index, then register it in AVAILABLE_TOOLS.\n"
            "Recommended free directions: DuckDuckGo HTML scrape (careful with ToS), "
            "or any free search API that does not require a credit card."
        )


# Registry of available tools (grows over time)
AVAILABLE_TOOLS: dict[str, type[Tool]] = {
    "echo": EchoTool,
    "local_time": LocalTimeTool,
    "system_info": SystemInfoTool,
    "list_dir": ListDirTool,
    "calc": CalcTool,
    "web_search": FreeSearchStubTool,
}


def get_tool(name: str) -> Tool | None:
    """Instantiate a tool by name."""
    cls = AVAILABLE_TOOLS.get(name)
    return cls() if cls else None


def list_tools() -> list[dict[str, str]]:
    """Return metadata for all registered tools."""
    return [
        {"name": cls.name, "description": cls.description}
        for cls in AVAILABLE_TOOLS.values()
    ]
