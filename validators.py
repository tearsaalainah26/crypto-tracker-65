import re

# Validation constraints for crypto assets
SUPPORTED_SYMBOLS = {'BTC', 'ETH', 'SOL', 'ADA', 'DOT'}

def validate_symbol(symbol: str) -> bool:
    """Validates asset ticker symbols against whitelist."""
    return isinstance(symbol, str) and symbol.upper() in SUPPORTED_SYMBOLS

def validate_amount(amount: float) -> bool:
    """Checks if trade amount is a positive numeric value."""
    return isinstance(amount, (int, float)) and amount > 0

def validate_request(data: dict) -> bool:
    """Entry point for payload sanitization in processing loop."""
    try:
        symbol = data.get('symbol')
        amount = data.get('amount')
        
        if not validate_symbol(symbol):
            return False
        
        if not validate_amount(amount):
            return False
            
        return True
    except (AttributeError, TypeError):
        return False

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass