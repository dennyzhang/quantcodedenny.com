#!/usr/bin/env python3
import os
import logging
import requests
import re
import google.generativeai as genai

# ----------------------
# Logger Setup
# ----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ----------------------
# Initialization
# ----------------------
def init_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable not set.")
        raise ValueError("Please set GEMINI_API_KEY in your environment.")
    
    genai.configure(api_key=api_key)
    logger.info("Gemini client initialized successfully.")
    return genai.GenerativeModel("gemini-2.5-pro")

# ----------------------
# SEC Filing Logic
# ----------------------
def get_sec_filings(ticker: str, filing_type="10-Q", count=1):
    cik_url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}&owner=exclude&action=getcompany&count={count}&output=atom"
    logger.info(f"Fetching SEC filings for {ticker} ({filing_type})...")
    
    resp = requests.get(cik_url, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code != 200:
        logger.warning(f"Failed to fetch filings: {resp.status_code}")
        return ""
    
    links = re.findall(r'<link href="(https://www.sec.gov/Archives/edgar/data/[^"]+\.txt)"', resp.text)
    if not links:
        logger.warning("No filings found.")
        return ""
    
    text_content = ""
    for link in links[:count]:
        r = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            text_content += r.text + "\n"
    
    logger.info(f"Fetched {len(links[:count])} filings for {ticker}.")
    return text_content

# ----------------------
# Prompt Generation
# ----------------------
def build_prompt(ticker: str, filing_text: str = "") -> str:
    prompt_template = f"""
Analyze recent news headlines and social media discussions for {ticker.upper()} from the past week and summarize:
1. Overall sentiment (Bullish / Neutral / Bearish)
2. Top 3 reasons driving this sentiment
3. Suggested action for a long-term tech investor (watch / buy / sell)
"""
    if filing_text:
        prompt_template += f"\nAdditionally, consider the following SEC filings content:\n{filing_text[:2000]}"

    prompt_template += "\nOutput as a concise bullet list."
    return prompt_template

# ----------------------
# Generate Sentiment
# ----------------------
def get_stock_sentiment(model, ticker: str, use_sec=True, use_llm=True) -> str:
    filing_text = ""
    if use_sec:
        filing_text = get_sec_filings(ticker)
    
    if use_llm:
        prompt = build_prompt(ticker, filing_text)
        logger.info(f"Generating sentiment for {ticker.upper()}...")
        response = model.generate_content(prompt)
        logger.info(f"Sentiment generation completed for {ticker.upper()}.")
        return response.text
    else:
        logger.info("LLM analysis skipped. Returning SEC filings only.")
        return filing_text or "No SEC filings available."

# ----------------------
# Main Function
# ----------------------
def main():
    ticker = os.getenv("STOCK_TICKER")
    if not ticker:
        logger.error("STOCK_TICKER environment variable not set.")
        exit(1)

    # Flags: read from environment
    use_sec = os.getenv("USE_SEC", "1") == "1"
    use_llm = os.getenv("USE_LLM", "1") == "1"

    try:
        model = init_gemini_client() if use_llm else None
        result = get_stock_sentiment(model, ticker, use_sec=use_sec, use_llm=use_llm)
        logger.info(f"=== {ticker.upper()} ===\n{result}")
    except Exception as e:
        logger.exception(f"Error occurred: {e}")

# ----------------------
# Entry Point
# ----------------------
if __name__ == "__main__":
    main()
