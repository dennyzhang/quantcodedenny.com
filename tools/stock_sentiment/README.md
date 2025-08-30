# setup env
```
# use docker

docker build -t denny/llm-stock-prompt .

export MY_GEMINI_API_KEY="sk-xxx"
export STOCK_TICKER="TSLA"
docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -v ./stock_sentiment.py:/app/stock_sentiment.py denny/llm-stock-prompt
```

# run unit test
```
make test
```

# functional test
```
# set env
export MY_GEMINI_API_KEY="sk-xxx"
export STOCK_TICKER="TSLA"

# only run sec filing parse
make run-sec

# only run llm prompt
make run-llm

# run all functions
make run-all
```

# run for real
```
bash-3.2$ export MY_GEMINI_API_KEY="sk-xxx"
bash-3.2$ export STOCK_TICKER="TSLA"
bash-3.2$ export GEMINI_MODEL="gemini-2.5-pro" # default one is gemini-1.5-flash
bash-3.2$ docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -e STOCK_TICKER="$STOCK_TICKER" -v .:/app/ denny/llm-stock-prompt
2025-08-30 06:51:01,730 [INFO] llm_utils.py:14 - Gemini client initialized successfully.
2025-08-30 06:51:02,510 [INFO] sec_utils.py:65 - Fetching filing from https://www.sec.gov/Archives/edgar/data/731766/000073176625000236/0000731766-25-000236.txt
2025-08-30 06:51:02,700 [INFO] sec_utils.py:68 - Successfully fetched filing for UNH.
2025-08-30 06:51:02,707 [INFO] main.py:21 - Extracted SEC sections for UNH (len=1283)
2025-08-30 06:51:02,707 [INFO] main.py:28 - Generating SEC sentiment for UNH...
2025-08-30 06:51:23,429 [INFO] main.py:32 - Generating headlines sentiment for UNH...
2025-08-30 06:51:46,990 [INFO] main.py:52 - === UNH ===
Based on an analysis of public discussions and the provided SEC filing metadata:

*   **Overall Market Sentiment: Neutral to Cautiously Bullish**
    *   The market recognizes UnitedHealth's dominant position and the long-term growth of its Optum health services segment. However, significant short-term headwinds from regulatory scrutiny and the recent cyberattack temper enthusiasm, leading to a neutral or cautiously optimistic stance. The provided SEC filing is a standard quarterly report header and does not, by itself, indicate positive or negative sentiment.

*   **Top 3 Sentiment Drivers:**
    1.  **Regulatory and Political Headwinds:** Ongoing DOJ antitrust investigations and scrutiny over Medicare Advantage reimbursement rates are significant sources of uncertainty and bearish pressure.
    2.  **Optum's Growth Engine:** The high-growth, high-margin Optum business (health services, tech, and PBM) remains the primary bullish driver, offering diversification from the core insurance business and exposure to health-tech innovation.
    3.  **Change Healthcare Cyberattack Fallout:** The recent major cyberattack creates significant short-term bearish sentiment due to remediation costs, reputational damage, and potential litigation, weighing against the company's strong fundamentals.

*   **Suggested Action for a Long-Term Tech Investor: Watch**
    *   UNH is a healthcare giant with a significant tech component (Optum). While this offers diversification, the primary risks are tied to healthcare policy and medical cost trends, not typical tech sector risks. Given the current regulatory uncertainty and the fallout from the cyberattack, it is prudent to monitor how the company navigates these challenges before initiating a position.

Based on an analysis of recent news, social media discussions, and the provided SEC filing information for UnitedHealth Group (UNH), here is a summary from the past week:

*   **Overall Sentiment: Bearish**
    *   While UNH remains a fundamentally strong company, the recent news cycle and discussions are dominated by significant headwinds and uncertainty, leading to a negative short-term outlook.

*   **Top 3 Reasons Driving This Sentiment:**
    1.  **Medicare Advantage (MA) Rate Pressure:** Persistent discussion surrounds the final 2025 Medicare Advantage payment rates from the government, which were lower than the industry had hoped. This is seen as a direct threat to the profitability of UNH's largest business segment, creating margin compression concerns.
    2.  **Fallout from the Change Healthcare Cyberattack:** The financial and operational impact of the massive cyberattack on its Optum unit continues to be a major topic. Discussions focus on the high costs of remediation, potential government fines and investigations, and lingering disruption for healthcare providers, all of which create a drag on earnings and introduce significant legal and regulatory risk.
    3.  **Elevated Medical Utilization Trends:** Broader industry data and analyst commentary continue to point towards higher-than-expected use of medical services, particularly among seniors. This trend directly increases costs for UNH, raising its medical loss ratio (MLR) and further squeezing profit margins.

*   **Suggested Action for a Long-Term Tech Investor: Watch**
    *   UNH is a healthcare giant, not a pure-play tech company. For a tech-focused investor, the current environment presents too many non-tech-related risks (regulatory, reimbursement, post-cyberattack litigation). The recommendation is to **Watch** from the sidelines until there is more clarity on how UNH navigates the margin pressure from MA rates and fully quantifies and resolves the financial and legal consequences of the Change Healthcare incident.

*   **Note on SEC Filing:**
    *   The provided SEC filing text is header information for a future quarterly report (10-Q) for the period ending June 30, 2025. It contains no substantive financial data or news and therefore does not influence current market sentiment.
bash-3.2$ 
```
