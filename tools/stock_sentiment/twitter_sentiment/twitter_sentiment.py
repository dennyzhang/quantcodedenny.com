#!/usr/bin/env python3
import os
import json
import subprocess
import sqlite3
import logging
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# ----------------------
# Logging Setup
# ----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)

DB_FILE = "sentiment.db"
OUTPUT_DIR = "outputs"

# ----------------------
# Helpers
# ----------------------
def load_follows(filepath="follows.txt"):
    logger.info(f"Loading follow list from {filepath}")
    with open(filepath) as f:
        return [line.strip() for line in f if line.strip()]

def fetch_tweets(user, limit=50):
    """Fetch tweets from a given user using snscrape"""
    logger.info(f"Fetching last {limit} tweets from user: {user}")
    cmd = f"snscrape --max-results {limit} twitter-user {user}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        logger.warning(f"Error fetching tweets for {user}: {result.stderr.strip()}")
        return []
    tweets = [line for line in result.stdout.splitlines() if line.strip()]
    logger.info(f"Fetched {len(tweets)} tweets for {user}")
    return tweets

def analyze_sentiment(text, analyzer):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "positive"
    elif score['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

def init_db():
    logger.info(f"Initializing database: {DB_FILE}")
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            user TEXT,
            tweet TEXT,
            sentiment TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    return conn

def save_to_db(conn, data, ticker):
    logger.info(f"Saving {len(data)} records to DB for {ticker}")
    cur = conn.cursor()
    for record in data:
        cur.execute(
            "INSERT INTO sentiments (ticker, user, tweet, sentiment, created_at) VALUES (?, ?, ?, ?, ?)",
            (ticker, record["user"], record["tweet"], record["sentiment"], datetime.utcnow().isoformat())
        )
    conn.commit()

# ----------------------
# Main Analysis
# ----------------------
def analyze_stock(ticker, follows_file="follows.txt"):
    logger.info(f"Starting sentiment analysis for: {ticker}")
    analyzer = SentimentIntensityAnalyzer()
    users = load_follows(follows_file)

    data = []
    for user in users:
        tweets = fetch_tweets(user, limit=30)
        for t in tweets:
            if ticker.lower() in t.lower():
                sentiment = analyze_sentiment(t, analyzer)
                data.append({"user": user, "tweet": t, "sentiment": sentiment})

    df = pd.DataFrame(data)
    if df.empty:
        logger.warning(f"No tweets found for ticker: {ticker}")
        return {"ticker": ticker, "tweets_analyzed": 0, "sentiment": {}}

    sentiment_counts = df["sentiment"].value_counts().to_dict()
    logger.info(f"Analyzed {len(df)} tweets. Sentiment distribution: {sentiment_counts}")

    # Save to DB
    conn = init_db()
    save_to_db(conn, data, ticker)

    # Save CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    csv_path = os.path.join(OUTPUT_DIR, f"sentiment_{ticker}_{datetime.today().date()}.csv")
    df.to_csv(csv_path, index=False)
    logger.info(f"Saved CSV to {csv_path}")

    return {
        "ticker": ticker,
        "tweets_analyzed": len(df),
        "sentiment": sentiment_counts,
        "tweets": df.to_dict(orient="records"),
    }

# ----------------------
# Entry Point
# ----------------------
if __name__ == "__main__":
    ticker = os.getenv("STOCK_TICKER")
    if not ticker:
        logger.error("STOCK_TICKER environment variable not set. Please export STOCK_TICKER.")
        raise ValueError("Please set the STOCK_TICKER environment variable, e.g., export STOCK_TICKER=TSLA")

    result = analyze_stock(ticker)
    logger.info(f"Analysis result:\n{json.dumps(result, indent=2)}")
