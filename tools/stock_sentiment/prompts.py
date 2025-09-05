def build_prompt_sec_filing(ticker: str, filing_text: str = "") -> str:
    snippet = filing_text[:8000] if filing_text else ""  # ~8k chars
    return f"""
Analyze sentiment for {ticker.upper()} combining public discussions and SEC filings.

Tasks:
1. Summarize overall market sentiment (Bullish / Neutral / Bearish).
2. Identify top 3 drivers behind this sentiment (e.g., product news, earnings, risks).
3. Provide a suggested action for a long-term tech investor (watch / buy / sell).

Key SEC Filing Highlights:
{snippet}

Return output as a concise bullet list.
"""

def build_prompt_headlines(ticker: str, filing_text: str = "") -> str:
    return f"""
Analyze recent news headlines and social media discussions for {ticker.upper()} from the past week and summarize:
1. Overall sentiment (Bullish / Neutral / Bearish)
2. Top 3 reasons driving this sentiment
3. Suggested action for a long-term tech investor (watch / buy / sell)

Additionally, consider the following SEC filings content:
{filing_text[:4000] if filing_text else ''}

Output as a concise bullet list.
"""
