import unittest
from unittest.mock import patch, MagicMock
import stock_sentiment_module as ssm  # replace with your file name without .py

class TestStockSentiment(unittest.TestCase):

    def test_build_prompt_includes_ticker(self):
        ticker = "TSLA"
        prompt = ssm.build_prompt(ticker, filing_text="Sample SEC content")
        self.assertIn(ticker, prompt)
        self.assertIn("Sample SEC content", prompt)

    @patch("stock_sentiment_module.requests.get")
    def test_get_sec_filings_returns_text(self, mock_get):
        # Mock SEC RSS feed response
        rss_content = '<link href="https://www.sec.gov/Archives/edgar/data/123456/filing1.txt"/>'
        mock_resp_rss = MagicMock(status_code=200, text=rss_content)
        # Mock the filing content
        mock_resp_filing = MagicMock(status_code=200, text="Filing Content Here")
        mock_get.side_effect = [mock_resp_rss, mock_resp_filing]

        result = ssm.get_sec_filings("TSLA", count=1)
        self.assertIn("Filing Content Here", result)

    @patch("stock_sentiment_module.genai.GenerativeModel.generate_content")
    @patch("stock_sentiment_module.get_sec_filings")
    def test_get_stock_sentiment_with_mocked_gemini(self, mock_filings, mock_generate_content):
        # Mock SEC filing text
        mock_filings.return_value = "SEC Filing Content"
        # Mock Gemini API response
        mock_generate_content.return_value = MagicMock(text="LLM Sentiment Output")

        model = MagicMock()  # fake model object
        sentiment = ssm.get_stock_sentiment(model, "TSLA")

        # Ensure the Gemini call was made
        mock_generate_content.assert_called_once()
        # Ensure sentiment text matches mock
        self.assertEqual(sentiment, "LLM Sentiment Output")

if __name__ == "__main__":
    unittest.main()
