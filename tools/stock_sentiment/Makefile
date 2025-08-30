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

.PHONY: run-sec
run-sec:
	@echo "Running for sec filing inside Docker..."
	@docker run --rm \
		-e GEMINI_API_KEY=$(GEMINI_API_KEY) \
		-e STOCK_TICKER=$(STOCK_TICKER) \
		-e USE_LLM=0 \
		-e USE_SEC=1 \
		-v $(PWD):/app \
		-w /app \
		$(DOCKER_IMAGE) \
		python stock_sentiment.py

.PHONY: run-llm
run-llm:
	@echo "Running for llm analysis Docker..."
	@docker run --rm \
		-e GEMINI_API_KEY=$(GEMINI_API_KEY) \
		-e STOCK_TICKER=$(STOCK_TICKER) \
		-e USE_LLM=1 \
		-e USE_SEC=0 \
		-v $(PWD):/app \
		-w /app \
		$(DOCKER_IMAGE) \
		python stock_sentiment.py


.PHONY: run-all
run-all:
	@echo "Running for all analysis Docker..."
	@docker run --rm \
		-e GEMINI_API_KEY=$(GEMINI_API_KEY) \
		-e STOCK_TICKER=$(STOCK_TICKER) \
		-e USE_LLM=1 \
		-e USE_SEC=1 \
		-v $(PWD):/app \
		-w /app \
		$(DOCKER_IMAGE) \
		python stock_sentiment.py
