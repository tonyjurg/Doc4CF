"""Provider configuration and authenticated request construction."""
import os
from urllib.request import Request


PROVIDERS = {
    "anthropic": ("Anthropic", "ANTHROPIC_API_KEY", "https://api.anthropic.com/v1/messages"),
    "openrouter": ("OpenRouter", "OPENROUTER_API_KEY", "https://openrouter.ai/api/v1/chat/completions"),
    "openai": ("OpenAI", "OPENAI_API_KEY", "https://api.openai.com/v1/chat/completions"),
    "groq": ("Groq", "GROQ_API_KEY", "https://api.groq.com/openai/v1/chat/completions"),
    "gemini": ("Google Gemini", "GEMINI_API_KEY", "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"),
}


def build_provider_request(provider: str, payload: bytes, offline_option: str) -> Request:
    """Build an authenticated JSON request for one configured provider."""
    _, key_name, endpoint = PROVIDERS[provider]
    api_key = os.environ.get(key_name)
    if not api_key:
        raise ValueError(f"Set {key_name} or omit {offline_option} for an offline build.")

    headers = {"Content-Type": "application/json"}
    if provider == "anthropic":
        headers.update({"x-api-key": api_key, "anthropic-version": "2023-06-01"})
        workspace = os.environ.get("ANTHROPIC_WORKSPACE_ID")
        if workspace:
            headers["anthropic-workspace-id"] = workspace
    else:
        headers["Authorization"] = f"Bearer {api_key}"
    return Request(endpoint, data=payload, headers=headers)
