"""Tools interface for GROK agents.

This layer is deliberately thin in v0.1 so it can grow into real
capabilities (web search, file system, APIs, memory) without breaking
the public Agent API.
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


# Registry of available tools (will grow)
AVAILABLE_TOOLS: dict[str, type[Tool]] = {
    "echo": EchoTool,
}


def get_tool(name: str) -> Tool | None:
    """Instantiate a tool by name."""
    cls = AVAILABLE_TOOLS.get(name)
    return cls() if cls else None
