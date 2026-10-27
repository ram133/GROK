"""GROK CLI — beautiful and fast."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel

from grok.core.agent import Agent

app = typer.Typer(
    name="grok",
    help="GROK — Personal AI Agent Toolkit",
    add_completion=False,
    rich_markup_mode="rich",
)
console = Console()


@app.command()
def run(
    task: str = typer.Argument(..., help="Natural language task for the agent"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress rich output"),
):
    """Run a task with the GROK agent."""
    agent = Agent()
    result = agent.run(task, verbose=not quiet)

    if quiet:
        print(result.output)


@app.command()
def version():
    """Show version."""
    from grok import __version__
    console.print(f"[bold]GROK[/] v{__version__}")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        console.print(Panel(
            "[bold cyan]GROK[/] — Personal AI Agent Toolkit\n\n"
            "Usage: [bold]grok \"your task here\"[/]\n\n"
            "Examples:\n"
            "  grok \"Research personal AI agent trends\"\n"
            "  grok \"Write a sharp LinkedIn post about shipping with AI\"\n"
            "  grok \"Make a 7-day plan to launch a side project\"",
            title="Welcome",
            border_style="cyan",
        ))


if __name__ == "__main__":
    app()
