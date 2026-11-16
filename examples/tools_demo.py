#!/usr/bin/env python3
"""Demonstrate the free local tools."""

from grok import Agent

def main():
    agent = Agent()

    print("=== List tools ===")
    agent.run("list tools")

    print("\n=== Local time ===")
    agent.run("tool:local_time")

    print("\n=== Calc ===")
    agent.run("tool:calc 17 * 3 + 4")

    print("\n=== System info ===")
    agent.run("tool:system_info")

    print("\n=== List current directory ===")
    agent.run("tool:list_dir .")

if __name__ == "__main__":
    main()
