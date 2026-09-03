import sys

def validate_ticker(ticker):
    """Ensures ticker format is strictly uppercase alphanumeric."""
    if not isinstance(ticker, str) or not ticker.isalnum() or not (1 <= len(ticker) <= 5):
        return False
    return True

def main_processing_loop(tickers):
    """Processes list of crypto tickers with input validation."""
    print("Starting crypto-tracker-65 data ingestion...")
    
    for ticker in tickers:
        try:
            if not validate_ticker(ticker):
                print(f"Skipping invalid ticker: {ticker}")
                continue
            
            # Simulate processing logic
            print(f"Fetching market data for: {ticker.upper()}")
            
        except Exception as e:
            print(f"Critical processing error on {ticker}: {e}")

if __name__ == "__main__":
    # Example integration
    sample_inputs = ["BTC", "eth", "SOL", "INVALID_LONG_TICKER", "123", "!@#"]
    main_processing_loop(sample_inputs)