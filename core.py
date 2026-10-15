import sys

def validate_ticker(ticker):
    """Ensures ticker is a valid alphanumeric string."""
    if not isinstance(ticker, str) or not ticker.isalnum() or len(ticker) < 2:
        return False
    return True

def process_market_data(tickers):
    """Main processing loop with input validation."""
    processed = []
    for ticker in tickers:
        if validate_ticker(ticker):
            # Simulating API fetch for crypto asset
            print(f"Fetching market data for: {ticker.upper()}")
            processed.append(ticker.upper())
        else:
            print(f"Skipping invalid ticker format: {ticker}")
    return processed

if __name__ == "__main__":
    # Mock input from external source
    raw_input = ["BTC", "ETH", "invalid_123", "SOL", "A"]
    
    print("Starting crypto-tracker-65 sync...")
    results = process_market_data(raw_input)
    print(f"Sync complete. Successfully processed: {len(results)} assets.")