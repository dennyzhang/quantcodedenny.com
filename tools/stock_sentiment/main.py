#!/usr/bin/env python3
import os
import logging
from sec_utils import get_sec_filings, extract_sec_key_sections
from prompts import build_prompt_sec_filing, build_prompt_headlines
from llm_utils import init_gemini_client, run_prompt

# Logger Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)

def get_stock_sentiment(model, ticker: str, use_sec=True, use_llm=True) -> str:
    filing_text = ""
    if use_sec:
        raw_filing = get_sec_filings(ticker)
        if raw_filing:
            filing_text = extract_sec_key_sections(raw_filing)
            logger.info(f"Extracted SEC sections for {ticker.upper()} (len={len(filing_text)})")

    if use_llm and model:
        results = []

        if filing_text:
            sec_prompt = build_prompt_sec_filing(ticker, filing_text)
            logger.info(f"Generating SEC sentiment for {ticker.upper()}...")
            results.append(run_prompt(model, sec_prompt))

        headlines_prompt = build_prompt_headlines(ticker, filing_text)
        logger.info(f"Generating headlines sentiment for {ticker.upper()}...")
        results.append(run_prompt(model, headlines_prompt))

        return "\n\n".join(results)

    logger.info("LLM analysis skipped. Returning SEC filings only.")
    return filing_text or "No SEC filings available."

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
