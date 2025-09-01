```
# [Only-once] Recreate the docker container
docker build -t denny/llm-stock-prompt .

# Use your own key
export GEMINI_API_KEYS="sk-xxx"
# Set stock code to evaluate
export STOCK_TICKER="RKLB"
# Use a powerful-yet-expensive model. Default is gemini-1.5-flash
export GEMINI_MODEL="gemini-2.5-pro"
# Run capability via docker
docker run --rm \
  -e GEMINI_API_KEYS="$GEMINI_API_KEYS" \
  -e STOCK_TICKER="$STOCK_TICKER" \
  -e GEMINI_MODEL="$GEMINI_MODEL" \
  -v .:/app/ \
  denny/llm-stock-prompt
```
