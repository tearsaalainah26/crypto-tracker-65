import sys

def validate_ticker(ticker):
    """Ensures ticker format is uppercase alphanumeric."""
    if not isinstance(ticker, str) or not ticker.isalnum():
        return False
    return len(ticker) >= 2

def process_market_data(ticker, amount):
    """Processes valid crypto market inputs."""
    if not validate_ticker(ticker):
        print(f"[Error] Invalid ticker format: {ticker}")
        return None
    
    try:
        val = float(amount)
        if val <= 0:
            raise ValueError
        return val
    except (ValueError, TypeError):
        print(f"[Error] Invalid amount provided: {amount}")
        return None

def main():
    """Main processing loop for crypto-tracker-65."""
    print("Crypto-Tracker-65 initializing...")
    
    inputs = [("BTC", 0.5), ("ETH", -1), ("INVALID!", 10)]
    
    for ticker, amount in inputs:
        result = process_market_data(ticker, amount)
        if result:
            print(f"Processed {ticker}: {result}")

if __name__ == "__main__":
    main()