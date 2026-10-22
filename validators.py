import re
from typing import Optional

def validate_ticker(ticker: str) -> bool:
    """Verify ticker symbol format (3-5 uppercase letters)."""
    if not isinstance(ticker, str):
        return False
    return bool(re.match(r'^[A-Z]{3,5}$', ticker))

def validate_price(price: float) -> bool:
    """Ensure price is a positive numerical value."""
    try:
        return isinstance(price, (int, float)) and price > 0
    except (TypeError, ValueError):
        return False

def sanitize_currency_code(code: str) -> Optional[str]:
    """Standardize currency code format to uppercase."""
    if not code or not isinstance(code, str):
        return None
    clean_code = code.strip().upper()
    return clean_code if len(clean_code) <= 4 else None

def is_valid_address(address: str, chain: str = 'BTC') -> bool:
    """Simple check for crypto address structure by chain."""
    patterns = {
        'BTC': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
        'ETH': r'^0x[a-fA-F0-9]{40}$'
    }
    pattern = patterns.get(chain.upper())
    if not pattern:
        return False
    return bool(re.match(pattern, address))