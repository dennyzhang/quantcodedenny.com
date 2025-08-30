# docker build -t llm-stock-prompt .
# Use a modern Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy your Python script
COPY stock_sentiment_demo.py .

# Set environment variable for OpenAI API key
# (Optional: can also pass at runtime)
ENV OPENAI_API_KEY="YOUR_API_KEY_HERE"

# Default command to run script
CMD ["python", "stock_sentiment_demo.py"]
