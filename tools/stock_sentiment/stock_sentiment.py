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
    model = genai.GenerativeModel("gemini-2.5-pro")
    return model

# ----------------------
# SEC Filing Logic
# ----------------------
def get_sec_filings(ticker: str, filing_type="10-Q", count=1):
    """
    Fetch recent SEC filings (default 10-Q) for the given ticker.
    Returns the plain text content of the most recent filings.
    """
    cik_url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}&owner=exclude&action=getcompany&count={count}&output=atom"
    logger.info(f"Fetching SEC filings for {ticker} ({filing_type}) from SEC RSS feed...")
    
    resp = requests.get(cik_url, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code != 200:
        logger.warning(f"Failed to fetch filings: {resp.status_code}")
        return ""
    
    # Extract filing links
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
def build_prompt(ticker: str, filing_text: str) -> str:
    """
    Build prompt including stock ticker and optional SEC filing content.
    """
    prompt_template = f"""
Analyze recent news headlines and social media discussions for {ticker.upper()} from the past week and summarize:
1. Overall sentiment (Bullish / Neutral / Bearish)
2. Top 3 reasons driving this sentiment
3. Suggested action for a long-term tech investor (watch / buy / sell)

Additionally, consider the following SEC filings content in your analysis:
{filing_text[:2000]}  # Truncate if too long for LLM

Output as a concise bullet list.
"""
    return prompt_template

# ----------------------
# Generate Sentiment
# ----------------------
def get_stock_sentiment(model, ticker: str) -> str:
    filing_text = get_sec_filings(ticker)
    prompt = build_prompt(ticker, filing_text)
    
    logger.info(f"Generating sentiment for {ticker.upper()}...")
    response = model.generate_content(prompt)
    logger.info(f"Sentiment generation completed for {ticker.upper()}.")
    return response.text

# ----------------------
# Main Function
# ----------------------
def main():
    ticker = os.getenv("STOCK_TICKER")
    if not ticker:
        logger.error("STOCK_TICKER environment variable not set.")
        exit(1)

    try:
        model = init_gemini_client()
        sentiment = get_stock_sentiment(model, ticker)
        logger.info(f"=== {ticker.upper()} ===\n{sentiment}")
    except Exception as e:
        logger.exception(f"Error occurred: {e}")

# ----------------------
# Entry Point
# ----------------------
if __name__ == "__main__":
    main()
