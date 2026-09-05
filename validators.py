import re

# Allowed cryptocurrency symbols for validation
VALID_SYMBOLS = {'BTC', 'ETH', 'SOL', 'ADA', 'DOT', 'XRP'}

def validate_ticker(symbol: str) -> bool:
    """Ensures symbol is uppercase and in supported list."""
    if not isinstance(symbol, str):
        return False
    return symbol.upper() in VALID_SYMBOLS

def validate_amount(amount: float) -> bool:
    """Checks for non-negative numerical input."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_api_key(key: str) -> bool:
    """Basic format validation for crypto exchange keys."""
    # Matches alphanumeric keys of length 32-64
    pattern = r'^[a-zA-Z0-9]{32,64}$'
    return bool(re.match(pattern, key))

def sanitize_input(user_input: str) -> str:
    """Removes whitespace and forces casing for uniformity."""
    return str(user_input).strip().upper()