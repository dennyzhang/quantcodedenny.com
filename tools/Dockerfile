# docker build -t denny/llm-stock-base .
# Use a modern Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements_base.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements_base.txt

# Set environment variable for OpenAI API key
# (Optional: can also pass at runtime)
ENV OPENAI_API_KEY="YOUR_API_KEY_HERE"

# Default command to run script
CMD ["echo", "hi there"]
