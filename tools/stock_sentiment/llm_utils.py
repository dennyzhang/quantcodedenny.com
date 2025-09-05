import logging
import os
import random
import google.generativeai as genai
from typing import List

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Environment config
# -----------------------------------------------------------------------------
def _load_api_keys() -> List[str]:
    """Load and validate Gemini API keys from environment."""
    raw = os.getenv("GEMINI_API_KEYS", "")
    keys = [k.strip() for k in raw.split(",") if k.strip()]
    if not keys:
        raise RuntimeError("No GEMINI_API_KEYS found in environment")
    return keys

def _load_model_name() -> str:
    """Return the Gemini model name from the environment variable GEMINI_MODEL."""
    return os.getenv("GEMINI_MODEL") or "gemini-1.5-flash"

# -----------------------------------------------------------------------------
# Random key selection
# -----------------------------------------------------------------------------
def _random_api_key() -> str:
    keys = _load_api_keys()
    key = random.choice(keys)
    logger.info(f"Using Gemini API key (masked): {key[:4]}...{key[-4:]}")
    return key

# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------
def init_gemini_client():
    """Configure and return a Gemini model client."""
    api_key = _random_api_key()
    genai.configure(api_key=api_key)

    model_name = _load_model_name()
    logger.info(f"Using Gemini model: {model_name}")
    return genai.GenerativeModel(model_name)

def run_prompt(model, prompt: str) -> str:
    """Run a text prompt against the given Gemini model."""
    response = model.generate_content(prompt)
    return getattr(response, "text", "")
