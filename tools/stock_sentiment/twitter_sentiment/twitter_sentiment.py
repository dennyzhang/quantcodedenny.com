import os
import logging
import tweepy

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Twitter API setup
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Stock ticker from env
ticker = os.getenv("STOCK_TICKER", "TSLA")
follows_file = "follows.txt"

# Load users
with open(follows_file) as f:
    users = [line.strip() for line in f.readlines() if line.strip()]

for user in users:
    try:
        # Get user ID
        user_obj = client.get_user(username=user)
        user_id = user_obj.data.id

        # Fetch recent tweets containing the ticker
        tweets = client.get_users_tweets(user_id, max_results=20, tweet_fields=["created_at","text"])
        logger.info(f"Fetched {len(tweets.data) if tweets.data else 0} tweets for {user}")
        for t in tweets.data or []:
            print(f"{t.created_at}: {t.text}")

    except Exception as e:
        logger.error(f"Error fetching tweets for {user}: {e}")
