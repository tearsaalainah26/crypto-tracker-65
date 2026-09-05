from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

def format_currency(amount: float, symbol: str = 'USD') -> str:
    """Formats a numerical value into a human-readable currency string."""
    try:
        return f"{amount:,.2f} {symbol}"
    except (ValueError, TypeError) as e:
        logger.error(f"Formatting error for amount {amount}: {e}")
        return f"0.00 {symbol}"

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculates the percentage change between two price points."""
    if previous == 0:
        return 0.0
    return ((current - previous) / abs(previous)) * 100

def sanitize_ticker(symbol: str) -> str:
    """Normalizes ticker symbols to uppercase alphanumeric format."""
    return "".join(char for char in symbol.upper() if char.isalnum())

def parse_api_response(data: Dict[str, Any], key: str) -> Optional[Any]:
    """Safely extracts a nested value from a crypto API response dict."""
    keys = key.split('.')
    current = data
    for k in keys:
        if isinstance(current, dict):
            current = current.get(k)
        else:
            return None
    return current