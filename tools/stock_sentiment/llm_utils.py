import os
import logging
import google.generativeai as genai

logger = logging.getLogger(__name__)

# Gemini Initialization
def init_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable not set.")
        raise ValueError("Please set GEMINI_API_KEY in your environment.")

    genai.configure(api_key=api_key)

    # Configurable model (default to cheaper model for testing)
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    # gemini-2.5-pro
    logger.info(f"Using Gemini model: {model_name}")
    return genai.GenerativeModel(model_name)

def run_prompt(model, prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text if response and hasattr(response, "text") else ""
