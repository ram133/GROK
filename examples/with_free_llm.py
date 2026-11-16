#!/usr/bin/env python3
"""Example: enable an optional free LLM backend.

This does NOT require a paid plan. Use any free OpenAI-compatible endpoint.

Examples of free endpoints (Nov 2026):
  - Groq:        https://api.groq.com/openai/v1
  - OpenRouter:  https://openrouter.ai/api/v1   (use models ending in :free)
  - Local Ollama: http://localhost:11434/v1

If the env vars are missing or the call fails, GROK falls back to its
local high-signal engine automatically.
"""

import os
from grok import Agent

def main():
    # Optional — comment these out and the local engine is used
    # os.environ["GROK_LLM_BASE_URL"] = "https://api.groq.com/openai/v1"
    # os.environ["GROK_LLM_API_KEY"] = "gsk_your_free_key"
    # os.environ["GROK_LLM_MODEL"] = "llama-3.3-70b-versatile"

    agent = Agent()
    result = agent.run("Write a 5-bullet summary of why free-first AI agents matter in 2026")
    print("Mode:", result.metadata.get("mode"))
    print(result.output)

if __name__ == "__main__":
    main()
