import os
import logging
import re
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
    """
    Loads sources to follow from the follows.txt file.
    It now ignores lines starting with a '#' character, as well as empty lines,
    and attempts to infer the source type if no prefix is provided.
    """
    if not os.path.exists(FOLLOWS_FILE):
        logger.critical(f"{FOLLOWS_FILE} not found. Please create it.")
        raise SystemExit(1)
    
    sources = []
    with open(FOLLOWS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            # Ignore comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # If no prefix, try to infer the source type
            if not any(line.startswith(prefix) for prefix in ["subreddit:", "user:"]):
                # Check for a user format (e.g., u/username)
                if re.match(r"^u/\w+$", line, re.IGNORECASE):
                    line = f"user:{line.lstrip('u/')}"
                # Otherwise, assume it's a subreddit
                else:
                    line = f"subreddit:{line}"
            sources.append(line)
            
    if not sources:
        logger.warning(f"No valid sources found in {FOLLOWS_FILE}.")
    return sources

# -----------------------------------------------------------------------------
# Reddit Client Init
# -----------------------------------------------------------------------------
def init_reddit():
    """Initializes the PRAW Reddit client."""
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")

    if not all([client_id, client_secret, user_agent]):
        logger.critical("Missing Reddit API credentials. Set REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT.")
        raise SystemExit(1)

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )
        # Test a simple read-only call to confirm connectivity
        logger.info(f"Reddit client initialized successfully.")
    except Exception as e:
        logger.critical(f"Reddit client initialization failed: {e}")
        raise SystemExit(1)

    return reddit

# -----------------------------------------------------------------------------
# Sentiment analysis
# -----------------------------------------------------------------------------
def analyze_sentiment(text):
    """Calculates the sentiment polarity of a given text."""
    blob = TextBlob(text)
    return blob.sentiment.polarity

# -----------------------------------------------------------------------------
# Fetch posts
# -----------------------------------------------------------------------------
def fetch_posts(reddit, source):
    """Fetches posts from a specified source (subreddit or user)."""
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
            # This block should now be unreachable due to load_follows changes
            logger.error(f"Invalid source format: {source}")
    except Exception as e:
        logger.error(f"Error fetching posts from {source}: {e}")

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    """Main function to run the sentiment analysis."""
    reddit = init_reddit()
    follows = load_follows()

    for source in follows:
        for text in fetch_posts(reddit, source):
            score = analyze_sentiment(text)
            logger.info(f"[{source}] {text} | Sentiment: {score:.2f}")

if __name__ == "__main__":
    main()
