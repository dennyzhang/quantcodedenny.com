# setup env
```
# use docker

docker build -t denny-llm-stock-prompt .

export MY_GEMINI_API_KEY="sk-xxx"
docker run -e GEMINI_API_KEY="$MY_GEMINI_API_KEY" -v ./stock_sentiment_demo.py:/app/stock_sentiment_demo.py llm-stock-prompt
```

# Sample output
```
bash-3.2$ docker run -e GEMINI_API_KEY="$MY_GEMINI_API_KEY" -v ./stock_sentiment_demo.py:/app/stock_sentiment_demo.py llm-stock-prompt
=== TSLA ===
Based on an analysis of financial news and social media discussions about TSLA from the past week:

*   **Overall Sentiment:** **Neutral**
    *   The sentiment is sharply divided. Negative sentiment is driven by current operational realities (sales, layoffs), while positive sentiment is fueled by future-looking, speculative catalysts (AI, Robotaxi). This creates a tense, neutral balance rather than a clear bullish or bearish trend.

*   **Top 3 Reasons Driving Sentiment:**
    1.  **Slowing EV Demand & Increased Competition (Bearish):** Recent data continues to show weak sales in key markets like China and Europe. This, combined with intense competition from Chinese automakers and ongoing price wars, is weighing heavily on the core auto business fundamentals.
    2.  **Anticipation for the 'Robotaxi' Unveiling and AI Progress (Bullish):** The primary bull case revolves around Tesla's pivot to an AI and robotics company. Hype is building for the August 8th Robotaxi reveal, and social media is filled with positive reviews of FSD (Supervised) V12, which bulls see as validation of Tesla's AI leadership.
    3.  **Corporate Instability and Strategic Uncertainty (Bearish):** Major recent layoffs, including the abrupt firing and subsequent partial rehiring of the Supercharger team, have created a narrative of chaotic management and strategic confusion. This uncertainty makes it difficult for investors to model the company's future growth and execution.

*   **Suggested Action for a Long-Term Tech Investor:** **Watch**
    *   The company is at a critical inflection point where its valuation is detaching from its current car sales and depending almost entirely on a future AI/robotics thesis. The risk/reward is unclear. It is prudent to wait for more concrete evidence of a turnaround in the core auto business or tangible details from the Robotaxi event before committing new capital.

=== NVDA ===
Based on an analysis of news and social media discussions surrounding NVDA this past week:

*   **Overall Sentiment:** Bullish
    *   *While the stock saw some profit-taking post-announcement, the underlying sentiment about the company's future and technology remains overwhelmingly positive.*

*   **Top 3 Reasons Driving Sentiment:**
    1.  **GTC Conference & Blackwell Unveiling:** The announcement of the next-generation "Blackwell" AI platform (B200 and GB200 GPUs) was the dominant topic. It promises a massive leap in performance, solidifying NVIDIA's technological lead in the AI hardware race and creating a clear future revenue stream.
    2.  **Strong Ecosystem Endorsement:** Major partners, including Amazon, Google, Microsoft, and Oracle, immediately announced plans to incorporate the new Blackwell chips into their cloud services and infrastructure. This widespread, immediate adoption by key customers validates the technology and de-risks its rollout.
    3.  **"Sell the News" Volatility:** The stock experienced a slight pullback immediately following the GTC keynote. This was widely interpreted not as a negative reaction to the news, but as a classic "buy the rumor, sell the fact" event and healthy consolidation after the stock's massive run-up, presenting a potential entry point for some investors.

*   **Suggested Action for a Long-Term Tech Investor:** Buy
    *   *The fundamental thesis for NVIDIA's dominance in the AI revolution was strengthened, not weakened, by this week's announcements. For an investor with a multi-year horizon, any price consolidation or dip should be viewed as a buying opportunity. Consider dollar-cost averaging to mitigate short-term volatility.*
```
