# setup env
```
# use docker

docker build -t llm-stock-prompt .

export MY_GEMINI_API_KEY="sk-xxx"
docker run -e GEMINI_API_KEY="$MY_GEMINI_API_KEY" -v ./stock_sentiment_demo.py:/app/stock_sentiment_demo.py llm-stock-prompt
```

# Sample output
```
bash-3.2$ docker run -e GEMINI_API_KEY="$MY_GEMINI_API_KEY" -v ./stock_sentiment_demo.py:/app/stock_sentiment_demo.py llm-stock-prompt
=== TSLA ===
Here is an analysis of recent TSLA news and discussions from the past week:

*   **Overall Sentiment:** Bearish (with a strong underlying bullish counter-narrative)

*   **Top 3 Reasons Driving Sentiment:**
    1.  **Weak Q1 Delivery Expectations:** The dominant story is the widespread concern over the upcoming Q1 delivery and production numbers. Analyst estimates have been repeatedly cut due to reported production reductions in China, sluggish demand in Europe, and a slowing EV market, leading to fears of a potential year-over-year decline.
    2.  **Intensifying Competition in China:** The high-profile and aggressively priced launch of Xiaomi's SU7 electric vehicle has amplified concerns about Tesla's market share and pricing power in its most critical market. This, combined with ongoing pressure from BYD, is fueling a narrative of a more difficult competitive landscape.
    3.  **Positive FSD v12 Momentum:** Acting as a powerful counter-narrative, social media and tech circles are buzzing with impressive demonstrations of the new Full Self-Driving (Supervised) v12. Bulls are touting this as a breakthrough moment for Tesla's AI development, reinforcing the long-term thesis that Tesla is more than just a car company.

*   **Suggested Action for a Long-Term Tech Investor:** Watch
    *   The significant short-term uncertainty around vehicle demand and upcoming delivery numbers presents a major risk. It is prudent to wait for the Q1 results to be released and see how the market digests the data before committing new capital. This allows an investor to assess if the current stock price weakness is a temporary issue or the beginning of a more fundamental downturn in growth.

=== NVDA ===
Here is a summary and analysis based on news and social media discussions about NVDA from the past week:

*   **Overall Sentiment:** **Bullish**
    *   The overwhelming sentiment is positive, driven by a recent major event and the continued strength of the company's core AI narrative. Bearish voices are present but are largely drowned out by excitement and momentum.

*   **Top 3 Reasons Driving Sentiment:**
    1.  **10-for-1 Stock Split:** The stock began trading at its split-adjusted price on June 10th. This has been the dominant topic, generating significant buzz among retail investors who see the lower share price as a more accessible entry point. It has also fueled speculation about NVDA's potential inclusion in the Dow Jones Industrial Average.
    2.  **Unwavering AI Leadership:** Discussions continue to center on NVDA's near-monopoly on AI training chips. The demand for its H100 and forthcoming Blackwell platform GPUs is seen as a durable, long-term trend, with analysts and investors confident in its massive growth runway in the data center market.
    3.  **Positive Analyst Revisions:** In the wake of the split and continued AI demand, several Wall Street analysts have reiterated "Buy" ratings and raised their price targets (on a split-adjusted basis), reinforcing institutional confidence and providing validation for the bullish retail sentiment.

*   **Suggested Action for a Long-Term Tech Investor:** **Buy (with a long-term perspective)**
    *   For an investor focused on the next 5-10 years, NVDA remains a core holding for exposure to the AI revolution. While the stock's valuation is high and short-term volatility is likely, the company's fundamental position as the leader in a transformative technology is undisputed. Consider dollar-cost averaging to build a position rather than investing a lump sum at all-time highs.
bash-3.2$ 
```
