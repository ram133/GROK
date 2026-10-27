#!/usr/bin/env python3
"""Quick demonstration of GROK."""

from grok import Agent

def main():
    agent = Agent()

    print("=== Example 1: Research ===")
    agent.run("Give me a sharp one-page brief on why personal AI agents will matter in 2026")

    print("\n=== Example 2: Content ===")
    agent.run("Write a short, high-signal LinkedIn post about treating AI as a co-worker instead of a toy")

    print("\n=== Example 3: Planning ===")
    agent.run("Create a realistic 7-day plan to launch a useful open-source AI tool")

if __name__ == "__main__":
    main()
