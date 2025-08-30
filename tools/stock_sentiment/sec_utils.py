# sec_utils.py
import logging
import requests
import re

logger = logging.getLogger(__name__)

# ----------------------
# CIK Lookup
# ----------------------
def get_cik_from_ticker(ticker: str) -> str | None:
    """
    Fetch CIK for a given ticker using SEC search.
    """
    headers = {"User-Agent": "YourCompanyName YourName@YourCompany.com"}
    try:
        search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}&Find=Search&owner=exclude&action=getcompany"
        resp = requests.get(search_url, headers=headers)
        resp.raise_for_status()
        match = re.search(r'CIK=(\d{10})', resp.text)
        if match:
            return match.group(1)
    except requests.RequestException as e:
        logger.error(f"Failed to find CIK: {e}")
    return None

# ----------------------
# Fetch SEC Filings
# ----------------------
def get_sec_filings(ticker: str, filing_type="10-Q", count=1) -> str:
    """
    Fetch the latest SEC filings for a given ticker.
    """
    try:
        cik = get_cik_from_ticker(ticker)
        if not cik:
            logger.error(f"CIK not found for ticker: {ticker}")
            return ""

        headers = {"User-Agent": "YourCompanyName YourName@YourCompany.com"} 
        submissions_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        submissions_resp = requests.get(submissions_url, headers=headers)
        submissions_resp.raise_for_status()
        submissions_data = submissions_resp.json()

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

        base_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
        accession_dir = target_accession_number.replace('-', '') + '/'
        submission_file = target_accession_number + '.txt'
        submission_url = base_url + accession_dir + submission_file

        logger.info(f"Fetching filing from {submission_url}")
        filing_resp = requests.get(submission_url, headers=headers)
        filing_resp.raise_for_status()
        logger.info(f"Successfully fetched filing for {ticker}.")

        return filing_resp.text[:20000]  # truncate for safety

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        return ""
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return ""

# ----------------------
# SEC Section Extraction & Cleaning
# ----------------------
def extract_sec_key_sections(filing_text: str) -> str:
    """
    Extract key sections from SEC filing: Risk Factors, MD&A, Financials
    """
    sections = {}

    match = re.search(r'ITEM\s+1A\.\s+RISK FACTORS(.*?)(?=ITEM\s+[1-9])', filing_text, re.S | re.I)
    if match:
        sections['Risk Factors'] = match.group(1).strip()

    match = re.search(r'ITEM\s+7\.\s+MANAGEMENT\'S DISCUSSION AND ANALYSIS(.*?)(?=ITEM\s+[1-9])', filing_text, re.S | re.I)
    if match:
        sections['MD&A'] = match.group(1).strip()

    match = re.search(r'ITEM\s+8\.\s+FINANCIAL STATEMENTS(.*?)(?=ITEM\s+[1-9])', filing_text, re.S | re.I)
    if match:
        sections['Financials'] = match.group(1).strip()

    if not sections:
        return clean_filing_text(filing_text[:5000])

    return "\n\n".join(f"{k}:\n{v[:2000]}" for k, v in sections.items())

def clean_filing_text(text: str) -> str:
    """
    Clean text by removing HTML tags, extra whitespace, and line breaks
    """
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
