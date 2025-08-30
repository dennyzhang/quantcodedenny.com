import os
import google.generativeai as genai

# Initialize Gemini client
api_key = os.getenv("GEMINI_API_KEY")  # <-- set this in your environment
print(f"api_key: {api_key}")
genai.configure(api_key=api_key)

# Load model (Gemini 2.5 Pro)
model = genai.GenerativeModel("gemini-2.5-pro")

# Prompt template
prompt_template = """
Analyze recent news headlines and social media discussions for {STOCK_TICKER} from the past week and summarize:
1. Overall sentiment (Bullish / Neutral / Bearish)
2. Top 3 reasons driving this sentiment
3. Suggested action for a long-term tech investor (watch / buy / sell)
Output as a concise bullet list.
"""

# Example stock tickers
tickers = ["TSLA", "NVDA"]

for ticker in tickers:
    prompt = prompt_template.replace("{STOCK_TICKER}", ticker)
    response = model.generate_content(prompt)
    
    print(f"\n=== {ticker} ===")
    print(response.text)   # .text gives the plain string output
