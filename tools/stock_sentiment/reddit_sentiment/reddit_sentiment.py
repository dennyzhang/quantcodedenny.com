import os
import logging
from textblob import TextBlob
import praw

# -----------------------------------------------------------------------------
# Logging setup (include filename and line number)
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
FOLLOWS_FILE = "follows.txt"
POST_LIMIT = int(os.getenv("POST_LIMIT", "10"))  # configurable via env

# -----------------------------------------------------------------------------
# Load follows.txt
# -----------------------------------------------------------------------------
def load_follows():
    if not os.path.exists(FOLLOWS_FILE):
        logger.critical(f"{FOLLOWS_FILE} not found. Please create it with sources (e.g. subreddit:wallstreetbets).")
        raise SystemExit(1)
    with open(FOLLOWS_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

# -----------------------------------------------------------------------------
# Reddit Client Init
# -----------------------------------------------------------------------------
def init_reddit():
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")

    if not all([client_id, client_secret, user_agent]):
        logger.critical("Missing Reddit API credentials. Set REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT.")
        raise SystemExit(1)

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )

    # Test authentication
    try:
        me = reddit.user.me()
        logger.info(f"Reddit authentication succeeded. Logged in as: {me}")
    except Exception as e:
        logger.critical(f"Reddit authentication failed: {e}")
        raise SystemExit(1)

    return reddit

# -----------------------------------------------------------------------------
# Sentiment analysis
# -----------------------------------------------------------------------------
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# -----------------------------------------------------------------------------
# Fetch posts
# -----------------------------------------------------------------------------
def fetch_posts(reddit, source):
    try:
        if source.startswith("subreddit:"):
            name = source.split(":", 1)[1]
            logger.info(f"Fetching posts from subreddit: {name}")
            for post in reddit.subreddit(name).hot(limit=POST_LIMIT):
                yield post.title
        elif source.startswith("user:"):
            name = source.split(":", 1)[1]
            logger.info(f"Fetching posts from user: {name}")
            for post in reddit.redditor(name).submissions.new(limit=POST_LIMIT):
                yield post.title
        else:
            logger.error(f"Invalid source format: {source}")
    except Exception as e:
        logger.error(f"Error fetching posts from {source}: {e}")

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    reddit = init_reddit()
    follows = load_follows()

    for source in follows:
        for text in fetch_posts(reddit, source):
            score = analyze_sentiment(text)
            logger.info(f"[{source}] {text} | Sentiment: {score:.2f}")

if __name__ == "__main__":
    main()
