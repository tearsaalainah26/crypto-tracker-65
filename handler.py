import logging

logger = logging.getLogger(__name__)

VALID_SYMBOLS = {'BTC', 'ETH', 'SOL', 'ADA'}

def validate_payload(data):
    """Ensures incoming crypto ticker data meets schema requirements."""
    if not isinstance(data, dict):
        return False, "payload must be a dictionary"
    
    symbol = data.get('symbol')
    price = data.get('price')

    if symbol not in VALID_SYMBOLS:
        return False, f"invalid symbol: {symbol}"
    
    if not isinstance(price, (int, float)) or price < 0:
        return False, f"invalid price value: {price}"

    return True, None

def process_ticker_updates(updates):
    """Main processing loop with integrated input validation."""
    for entry in updates:
        is_valid, error = validate_payload(entry)
        
        if not is_valid:
            logger.warning(f"skipping invalid record: {error}")
            continue
        
        # Process validated market data
        symbol = entry['symbol']
        price = entry['price']
        logger.info(f"processing {symbol} at ${price:.2f}")

if __name__ == "__main__":
    mock_data = [
        {'symbol': 'BTC', 'price': 50000.0},
        {'symbol': 'DOGE', 'price': 0.1},
        {'symbol': 'ETH', 'price': -100},
        {'symbol': 'SOL', 'price': 150.5}
    ]
    process_ticker_updates(mock_data)