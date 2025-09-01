# docker build -t denny/llm-stock-prompt .
FROM denny/llm-stock-base:latest

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy your Python script
COPY *.py .

# Set environment variable for OpenAI API key
# (Optional: can also pass at runtime)
ENV OPENAI_API_KEY="YOUR_API_KEY_HERE"

ENV STOCK_TICKER="YOUR_STOCK_TICKER"

# Default command to run script
CMD ["python", "twitter_sentiment.py"]
