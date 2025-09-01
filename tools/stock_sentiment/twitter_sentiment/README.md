```
# [Only-once] Recreate the docker container
docker build -t denny/llm-stock-prompt .

# Use your own key
export GEMINI_API_KEYS="sk-xxx"
# Set stock code to evaluate
export STOCK_TICKER="RKLB"
# Twitter Bearer Token
export TWITTER_BEARER_TOKEN="AAAxxx"
# Run capability via docker
docker run --rm \
  -e TWITTER_BEARER_TOKEN="$TWITTER_BEARER_TOKEN" \
  -e STOCK_TICKER="$STOCK_TICKER" \
  -v .:/app/ \
  denny/llm-stock-prompt
```
