"""Optional free-tier LLM backend for GROK.

Prime directive: FREE.
- No key required → local high-signal patterns are used.
- Set env vars to enable any OpenAI-compatible free endpoint
  (Groq, OpenRouter :free models, Google AI Studio via proxy, etc.).

Env vars:
  GROK_LLM_BASE_URL   e.g. https://api.groq.com/openai/v1
  GROK_LLM_API_KEY    your free key
  GROK_LLM_MODEL      model id (e.g. llama-3.3-70b-versatile or any :free model)
"""

from __future__ import annotations

import os
from typing import Any

try:
    import httpx
except ImportError:  # pragma: no cover
    httpx = None  # type: ignore


def llm_available() -> bool:
    """True if free LLM env vars are configured."""
    return bool(
        os.getenv("GROK_LLM_BASE_URL")
        and os.getenv("GROK_LLM_API_KEY")
        and os.getenv("GROK_LLM_MODEL")
        and httpx is not None
    )


def call_llm(prompt: str, *, system: str | None = None, max_tokens: int = 1024) -> str | None:
    """Call the configured free LLM. Returns None on any failure so caller can fall back."""
    if not llm_available():
        return None

    base = os.environ["GROK_LLM_BASE_URL"].rstrip("/")
    key = os.environ["GROK_LLM_API_KEY"]
    model = os.environ["GROK_LLM_MODEL"]

    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    url = f"{base}/chat/completions"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.4,
    }

    try:
        with httpx.Client(timeout=45.0) as client:
            r = client.post(url, headers=headers, json=payload)
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"].strip()
    except Exception:
        # Silent failure → caller falls back to local engine
        return None
