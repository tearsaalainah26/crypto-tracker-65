import logging

def validate_ticker(ticker):
    """Checks if ticker format is valid (alphanumeric, 2-10 chars)."""
    if not isinstance(ticker, str) or not (2 <= len(ticker) <= 10):
        return False
    return ticker.isalnum()

def process_crypto_data(payload):
    """
    Main processing loop for incoming crypto updates.
    Validates ticker symbol and numeric price before aggregation.
    """
    ticker = payload.get('ticker')
    price = payload.get('price')

    # Validate input schema and data integrity
    if not validate_ticker(ticker):
        logging.error(f"Invalid ticker received: {ticker}")
        return False

    try:
        price_val = float(price)
        if price_val < 0:
            raise ValueError("Negative price value")
    except (TypeError, ValueError) as e:
        logging.error(f"Invalid price format for {ticker}: {e}")
        return False

    # Perform core tracking logic
    update_database(ticker.upper(), price_val)
    return True

def update_database(ticker, price):
    """Placeholder for persistence layer operations."""
    print(f"Updating {ticker} with price {price}")