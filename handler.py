import logging

logger = logging.getLogger(__name__)

def validate_ticker(ticker):
    """Checks if ticker format is valid."""
    if not isinstance(ticker, str) or len(ticker) < 2 or len(ticker) > 10:
        return False
    return ticker.isalnum()

def process_crypto_updates(data_stream):
    """
    Main processing loop for incoming crypto price feeds.
    Validates input before proceeding to business logic.
    """
    for entry in data_stream:
        try:
            ticker = entry.get("ticker")
            price = entry.get("price")

            # Input validation checks
            if not validate_ticker(ticker):
                logger.warning(f"Invalid ticker format: {ticker}")
                continue

            if not isinstance(price, (int, float)) or price < 0:
                logger.warning(f"Invalid price value: {price} for {ticker}")
                continue

            # Process valid ticker and price
            logger.info(f"Updating {ticker} to {price}")
            
        except Exception as e:
            logger.error(f"Unexpected error during processing: {e}")

if __name__ == "__main__":
    sample_data = [{"ticker": "BTC", "price": 50000}, {"ticker": "!INVALID", "price": 10}]
    process_crypto_updates(sample_data)