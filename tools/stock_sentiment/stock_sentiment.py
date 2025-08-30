#!/usr/bin/env python3
import os
import logging
import google.generativeai as genai
from sec_utils import get_sec_filings, extract_sec_key_sections

# Logger Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)

# Gemini Initialization
def init_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable not set.")
        raise ValueError("Please set GEMINI_API_KEY in your environment.")
    
    genai.configure(api_key=api_key)
    logger.info("Gemini client initialized successfully.")
    return genai.GenerativeModel("gemini-2.5-pro")

# Prompt Generation
def build_prompt(ticker: str, filing_text: str = "") -> str:
    prompt = f"""
Analyze recent news headlines and social media discussions for {ticker.upper()} from the past week and summarize:
1. Overall sentiment (Bullish / Neutral / Bearish)
2. Top 3 reasons driving this sentiment
3. Suggested action for a long-term tech investor (watch / buy / sell)
"""
    if filing_text:
        prompt += f"\nAdditionally, consider the following SEC filings content:\n{filing_text}"
    prompt += "\nOutput as a concise bullet list."
    return prompt

# Stock Sentiment Generation
def get_stock_sentiment(model, ticker: str, use_sec=True, use_llm=True) -> str:
    filing_text = ""
    if use_sec:
        raw_filing = get_sec_filings(ticker)
        if raw_filing:
            filing_text = extract_sec_key_sections(raw_filing)

    if use_llm and model:
        prompt = build_prompt(ticker, filing_text)
        logger.info(f"Generating sentiment for {ticker.upper()}...")
        response = model.generate_content(prompt)
        logger.info(f"Sentiment generation completed for {ticker.upper()}.")
        return response.text
    else:
        logger.info("LLM analysis skipped. Returning SEC filings only.")
        return filing_text or "No SEC filings available."

# Main Function
def main():
    ticker = os.getenv("STOCK_TICKER")
    if not ticker:
        logger.error("STOCK_TICKER environment variable not set.")
        exit(1)

    use_sec = os.getenv("USE_SEC", "1") == "1"
    use_llm = os.getenv("USE_LLM", "1") == "1"

    try:
        model = init_gemini_client() if use_llm else None
        result = get_stock_sentiment(model, ticker, use_sec=use_sec, use_llm=use_llm)
        logger.info(f"=== {ticker.upper()} ===\n{result}")
    except Exception as e:
        logger.exception(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
