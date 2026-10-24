import time
from typing import Dict, Optional, Any

def format_currency(amount: float, symbol: str = 'USD') -> str:
    """Formats a numerical crypto balance as a currency string."""
    return f"{amount:,.4f} {symbol}"

def calculate_profit(initial: float, current: float) -> float:
    """Calculates percentage profit given initial and current price."""
    if initial == 0:
        return 0.0
    return ((current - initial) / initial) * 100

def get_timestamp() -> int:
    """Returns the current epoch timestamp as an integer."""
    return int(time.time())

def sanitize_ticker(ticker: str) -> str:
    """Standardizes ticker symbols to uppercase."""
    return ticker.strip().upper()

def parse_response(data: Dict[str, Any], key: str) -> Optional[Any]:
    """Safely extracts values from API response dictionaries."""
    try:
        return data.get(key)
    except AttributeError:
        return None