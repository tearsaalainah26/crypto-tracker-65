import logging
from typing import Dict, Any, Optional

# Configure logger for tracking operations
logger = logging.getLogger('crypto-tracker-65')

def format_price(amount: float, precision: int = 2) -> str:
    """Formats crypto price to currency string."""
    return f"${amount:,.{precision}f}"

def validate_ticker(ticker: str) -> bool:
    """Checks if ticker format is valid uppercase."""
    return isinstance(ticker, str) and ticker.isalpha() and ticker.isupper()

def normalize_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes API response dictionaries."""
    return {
        'symbol': raw_data.get('s', 'UNKNOWN'),
        'price': float(raw_data.get('p', 0.0)),
        'volume': float(raw_data.get('v', 0.0)),
        'timestamp': raw_data.get('t')
    }

def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Access nested data safely with defaults."""
    try:
        return data.get(key, default)
    except AttributeError:
        logger.error(f"Invalid data structure provided for key: {key}")
        return default