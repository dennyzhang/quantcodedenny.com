# Makefile

# Environment variables (can override in terminal)
GEMINI_API_KEY ?= sk-test
STOCK_TICKER ?= TSLA

# Docker image name
DOCKER_IMAGE ?= denny/llm-stock-prompt

# Default target: run unit tests inside Docker
.PHONY: test
test:
	@echo "Running unit tests inside Docker..."
	@docker run --rm \
		-e GEMINI_API_KEY=$(GEMINI_API_KEY) \
		-e STOCK_TICKER=$(STOCK_TICKER) \
		-v $(PWD):/app \
		-w /app \
		$(DOCKER_IMAGE) \
		python -m unittest -v test_stock_sentiment.py
