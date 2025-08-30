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
bash-3.2$  docker run --rm -e GEMINI_API_KEY="$GEMINI_API_KEY" -e STOCK_TICKER="$STOCK_TICKER" -v ./stock_sentiment.py:/app/stock_sentiment.py denny/llm-stock-prompt
2025-08-30 06:24:08,378 [INFO] stock_sentiment.py:22 - Gemini client initialized successfully.
2025-08-30 06:24:08,702 [INFO] sec_utils.py:65 - Fetching filing from https://www.sec.gov/Archives/edgar/data/1318605/000162828025035806/0001628280-25-035806.txt
2025-08-30 06:24:09,011 [INFO] sec_utils.py:68 - Successfully fetched filing for TSLA.
2025-08-30 06:24:09,017 [INFO] stock_sentiment.py:48 - Generating sentiment for TSLA...
2025-08-30 06:24:34,474 [INFO] stock_sentiment.py:50 - Sentiment generation completed for TSLA.
2025-08-30 06:24:34,475 [INFO] stock_sentiment.py:69 - === TSLA ===
Based on an analysis of recent news, social media trends, and the provided (future-dated) SEC filing information from the past week:

*   **SEC Filing Note:** The provided SEC filing `0001628280-25-035806.txt` is a header for a Q2 2025 10-Q report. As its reporting period is in the future, it contains no financial data or substantive information for current analysis.

Here is the summary of recent discussions:

*   **Overall Sentiment:** **Neutral**
    *   The sentiment is highly polarized, with strong bearish and bullish camps creating a neutral balance. Near-term operational challenges are being weighed against a high-risk, high-reward future narrative.

*   **Top 3 Reasons Driving This Sentiment:**
    1.  **Bearish: Slowing Growth and Increased Competition.** Recent delivery numbers were a significant miss, showing a year-over-year decline for the first time since 2020. This has fueled concerns about weakening global EV demand, market saturation for premium models, and intense pressure from competitors like BYD in key markets.
    2.  **Bullish: The "Robotaxi" Catalyst.** Elon Musk's announcement of a Robotaxi unveil event on August 8th has massively shifted the narrative. This focuses investor attention away from short-term car sales and towards Tesla's potential as a long-term AI and robotics company, which bulls argue justifies a much higher valuation.
    3.  **Uncertainty: Strategic Shift & FSD Progress.** The company's heavy emphasis on the Robotaxi and Full Self-Driving (FSD)—including wider software releases and subscription pushes—is seen as a pivotal bet. Bulls see accelerating progress towards autonomy, while bears point to the significant technological and regulatory hurdles that remain, viewing the strategy as a risky distraction from solving core manufacturing and demand issues.

*   **Suggested Action for a Long-Term Tech Investor:** **Watch**
    *   Tesla is at a critical inflection point. For a long-term investor, selling now could mean missing a potential paradigm shift if the Robotaxi/AI bet pays off. However, buying aggressively is risky given the clear headwinds in the core auto business. The most prudent action is to watch for tangible progress on FSD, concrete details from the August Robotaxi event, and signs of stabilization in vehicle demand before committing new capital.
```
