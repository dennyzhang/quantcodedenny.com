# setup env
```
# use docker

docker build -t denny/llm-stock-prompt .

export MY_GEMINI_API_KEY="sk-xxx"
docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -v ./stock_sentiment.py:/app/stock_sentiment.py denny/llm-stock-prompt
```

# run unit test
```
make test
```

# functional test
```
# only run sec filing parse
make run-sec

# only run llm prompt
make run-llm

# run all functions
make run-all
```

# run for real
```
bash-3.2$ export STOCK_TICKER="TSLA"
bash-3.2$ docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -e STOCK_TICKER="$STOCK_TICKER" -v ./stock_sentiment.py:/app/stock_sentiment.py denny/llm-stock-prompt
2025-08-30 05:45:35,011 [INFO] Gemini client initialized successfully.
2025-08-30 05:45:35,011 [INFO] Fetching SEC filings for TSLA (10-Q) from SEC RSS feed...
2025-08-30 05:45:35,195 [WARNING] Failed to fetch filings: 403
2025-08-30 05:45:35,196 [INFO] Generating sentiment for TSLA...
2025-08-30 05:45:56,117 [INFO] Sentiment generation completed for TSLA.
2025-08-30 05:45:56,117 [INFO] === TSLA ===
Here is a concise analysis of TSLA based on news and discussions from the past week:

*   **Overall Sentiment: Bearish**
    *   The prevailing sentiment is dominated by uncertainty and risk, leaning bearish ahead of a pivotal shareholder meeting. While a dedicated bull case exists, the near-term headwinds and governance concerns are the primary focus of most discussions.

*   **Top 3 Reasons Driving This Sentiment:**
    1.  **Shareholder Vote Controversy:** The upcoming vote on Elon Musk's ~$56B compensation package and the company's reincorporation to Texas is the single largest driver. Major proxy advisory firms (ISS, Glass Lewis) have recommended voting against the pay package, creating a significant conflict with retail shareholders and the board. The outcome is uncertain and perceived as a referendum on Musk's leadership, creating stock volatility.
    2.  **Slowing Growth vs. AI Pivot:** Recent news continues to highlight slowing EV sales growth and increased competition, particularly from China (underscored by new US tariffs). In response, Musk has intensified his narrative that Tesla is an "AI & Robotics company," not a car company. This strategic pivot creates a valuation dilemma: investors are weighing tangible, slowing auto revenues against a more speculative, long-term bet on robotaxis and Optimus.
    3.  **Institutional & Analyst Concerns:** Several analysts have recently cut price targets or delivery estimates, citing weakening demand and the long road to realizing FSD/robotaxi revenue. These concerns are amplified by the content of the **Proxy Statement (DEF 14A)**, which details the board's justifications for the controversial votes but also highlights the governance risks that worry institutional investors.

*   **Suggested Action for a Long-Term Tech Investor: Watch**
    *   The immense near-term uncertainty makes initiating or adding to a position risky. The outcome of the June 13th shareholder meeting will be a critical catalyst. **Watch** for the results of the vote and the market's reaction. This event will provide significant clarity on shareholder confidence, corporate governance, and Musk's future focus, allowing for a more informed long-term investment decision.
```
