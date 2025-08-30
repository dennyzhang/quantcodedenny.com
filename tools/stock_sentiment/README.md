This tool empowers engineers to automate stock sentiment analysis with precision and speed. It combines two core capabilities: parsing recent news headlines to extract market sentiment and insights, and parsing SEC filings to surface key financial and risk information. Both streams are fed into a configurable LLM pipeline, allowing you to run fast local tests with lightweight models or perform high-accuracy production analysis. Designed for modularity and reuse, it integrates seamlessly into your workflows—turning raw data into actionable insights without manual reading.

# 1 Setup env
- Install docker in your laptop
- Apply for GEMINI_API_KEY

# 2 Run for real
```
# Use your own key
export GEMINI_API_KEY="sk-xxx"
# Set stock code to evaluate
export STOCK_TICKER="UNH"
# Use a powerful-yet-expensive model. Default is gemini-1.5-flash
export GEMINI_MODEL="gemini-2.5-pro"
# Run capability via docker
docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -e STOCK_TICKER="$STOCK_TICKER" -e GEMINI_MODEL="$GEMINI_MODEL" -v .:/app/ denny/llm-stock-prompt

2025-08-30 06:51:01,730 [INFO] llm_utils.py:14 - Gemini client initialized successfully.
2025-08-30 06:51:02,510 [INFO] sec_utils.py:65 - Fetching filing from https://www.sec.gov/Archives/edgar/data/731766/000073176625000236/0000731766-25-000236.txt
2025-08-30 06:51:02,700 [INFO] sec_utils.py:68 - Successfully fetched filing for UNH.
2025-08-30 06:51:02,707 [INFO] main.py:21 - Extracted SEC sections for UNH (len=1283)
2025-08-30 06:51:02,707 [INFO] main.py:28 - Generating SEC sentiment for UNH...
2025-08-30 06:51:23,429 [INFO] main.py:32 - Generating headlines sentiment for UNH...
2025-08-30 06:51:46,990 [INFO] main.py:52 - === UNH ===
```

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

  
# 3 [Optional] Local CI/CD
```
# Run unit test
make test

# Function test: sec filing parse only
make run-sec

# Function test: llm prompt only
make run-llm

# Function test: all
make run-all
```
