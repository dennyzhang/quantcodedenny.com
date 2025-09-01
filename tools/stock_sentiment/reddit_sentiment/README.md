```
# [Only-once] Recreate the docker container
docker build -t denny/llm-reddit-sentiment .

export REDDIT_CLIENT_ID="your_id"
export REDDIT_CLIENT_SECRET="your_secret"
export REDDIT_USER_AGENT="my-reddit-sentiment-app"

# Run capability via docker
docker run --rm \
  -e REDDIT_CLIENT_ID="$REDDIT_CLIENT_ID" \
  -e REDDIT_CLIENT_SECRET="$REDDIT_CLIENT_SECRET" \
  -e REDDIT_USER_AGENT="$REDDIT_USER_AGENT" \
  -v .:/app/ \
  denny/llm-reddit-sentiment
```
