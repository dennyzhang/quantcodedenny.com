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
bash-3.2$  docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -e STOCK_TICKER="$STOCK_TICKER" -v ./stock_sentiment.py:/app/stock_sentiment.py denny/llm-stock-prompt
2025-08-30 06:03:35,224 [INFO] Gemini client initialized successfully.
2025-08-30 06:03:35,225 [INFO] Fetching SEC filings for TSLA (10-Q)...
2025-08-30 06:03:35,398 [WARNING] Failed to fetch filings: 403
2025-08-30 06:03:35,399 [INFO] Generating sentiment for TSLA...
2025-08-30 06:03:58,635 [INFO] Sentiment generation completed for TSLA.
2025-08-30 06:03:58,635 [INFO] === TSLA ===
Based on an analysis of news headlines and social media discussions about TSLA from the past week:

*   **Overall Sentiment: Neutral**
    *   The sentiment is highly polarized, with strong bearish arguments based on current fundamentals clashing with strong bullish arguments based on future potential. This creates a tense, neutral balance with high volatility.

*   **Top 3 Reasons Driving Sentiment:**
    1.  **Bullish Catalyst - Robotaxi Event:** The announcement of a dedicated Robotaxi reveal on August 8th is the primary driver of positive sentiment. It focuses discussion on Tesla's future as an AI and robotics company, shifting the narrative away from current car sales figures.
    2.  **Bearish Headwind - Slowing Demand & Layoffs:** Persistent concerns over slowing EV sales, increased competition, and the impact of recent mass layoffs (including the Supercharger team) are driving the negative case, raising questions about core business health and margins.
    3.  **Critical Uncertainty - Shareholder Vote:** The upcoming June 13th shareholder meeting is a major point of focus. The vote on Elon Musk's compensation package and the move to reincorporate in Texas is seen as a referendum on his leadership, creating significant uncertainty and a major potential catalyst in either direction.

*   **Suggested Action for a Long-Term Tech Investor: Watch**
    *   The company is at a critical inflection point. It is prudent to wait for more clarity from the shareholder vote in June and the Robotaxi event in August before committing new capital. These events will provide crucial data on institutional support for Musk's vision and the tangible progress of the company's AI ambitions.
```
