"""Tools interface for GROK agents.

Prime directive: FREE. The base layer requires zero paid services.
Optional free-tier LLM / search backends can be plugged in later.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
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


# Registry of available tools (grows over time)
AVAILABLE_TOOLS: dict[str, type[Tool]] = {
    "echo": EchoTool,
    "local_time": LocalTimeTool,
    "system_info": SystemInfoTool,
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
