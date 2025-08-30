import os
import logging
import requests
import re
import google.generativeai as genai
import time

# ----------------------
# Logger Setup
# ----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
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
    """
    Fetches the latest SEC filings for a given ticker using the new SEC API.
    """
    try:
        cik = get_cik_from_ticker(ticker)
        if not cik:
            logger.error(f"CIK not found for ticker: {ticker}")
            return ""

        logger.info(f"Found CIK {cik} for {ticker}.")

        # Step 2: Use the submissions history API to find the latest 10-Q filing
        submissions_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        
        headers = {"User-Agent": "YourCompanyName YourName@YourCompany.com"} 
        submissions_resp = requests.get(submissions_url, headers=headers)
        submissions_resp.raise_for_status()
        
        submissions_data = submissions_resp.json()
        
        # Find the latest 10-Q filing
        filings = submissions_data.get('filings', {}).get('recent', {})
        accession_numbers = filings.get('accessionNumber', [])
        form_types = filings.get('form', [])
        
        target_accession_number = None
        for i, form_type in enumerate(form_types):
            if form_type == filing_type:
                target_accession_number = accession_numbers[i]
                break

        if not target_accession_number:
            logger.warning(f"No recent {filing_type} filings found for {ticker}.")
            return ""

        logger.info(f"Found accession number {target_accession_number} for {ticker}.")

        # Step 3: Construct the URL and fetch the filing text
        # Correct URL format includes the accession number without dashes as a directory
        base_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
        accession_dir = target_accession_number.replace('-', '') + '/'
        submission_file = target_accession_number + '.txt'
        
        submission_url = base_url + accession_dir + submission_file
        
        logger.info(f"Fetching filing from {submission_url}")
        filing_resp = requests.get(submission_url, headers=headers)
        filing_resp.raise_for_status()

        text_content = filing_resp.text
        logger.info(f"Successfully fetched filing for {ticker}.")
        
        return text_content[:20000]
        
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        return ""
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        return ""

# New function to handle the CIK lookup more reliably
def get_cik_from_ticker(ticker):
    """
    Attempts to get the CIK from a direct search on the SEC's website.
    This is more reliable than parsing the company_tickers.json file.
    """
    headers = {"User-Agent": "YourCompanyName YourName@YourCompany.com"}
    
    try:
        search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}&Find=Search&owner=exclude&action=getcompany"
        
        resp = requests.get(search_url, headers=headers)
        resp.raise_for_status()

        cik_match = re.search(r'CIK=(\d{10})', resp.text)
        if cik_match:
            return cik_match.group(1)
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to find CIK via SEC search: {e}")

    return None

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
