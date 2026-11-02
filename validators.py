import re

def validate_ticker(ticker: str) -> bool:
    """Ensures ticker follows standard uppercase format."""
    if not isinstance(ticker, str):
        return False
    return bool(re.match(r'^[A-Z0-9]{1,10}$', ticker))

def validate_price(price: float) -> bool:
    """Checks if price is a positive numerical value."""
    try:
        val = float(price)
        return val >= 0
    except (ValueError, TypeError):
        return False

def validate_payload(data: dict) -> bool:
    """Basic validation for incoming crypto market data."""
    required_fields = ['ticker', 'price', 'volume']
    if not all(field in data for field in required_fields):
        return False
    
    if not validate_ticker(data['ticker']):
        return False
    
    if not validate_price(data['price']):
        return False
        
    return True