import decimal
from typing import Union

def format_currency(value: Union[float, str, decimal.Decimal], precision: int = 2) -> str:
    """Formats crypto price or balance values to standard strings."""
    val = decimal.Decimal(str(value))
    return f"{val:.{precision}f}"

def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculates simple percentage change between two values."""
    if old_value == 0:
        return 0.0
    return ((new_value - old_value) / abs(old_value)) * 100

def validate_ticker(ticker: str) -> bool:
    """Ensures ticker format matches uppercase alphanumeric requirements."""
    return bool(ticker and ticker.isalnum() and ticker.isupper())

def format_asset_pair(base: str, quote: str = "USD") -> str:
    """Standardizes ticker pairs for API requests."""
    return f"{base.upper()}/{quote.upper()}"

def sanitize_float(value: any) -> float:
    """Safely converts input to float for trading calculations."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0