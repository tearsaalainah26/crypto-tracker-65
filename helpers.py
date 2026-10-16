import decimal
from typing import Union

def format_currency(value: Union[float, str, decimal.Decimal], precision: int = 2) -> str:
    """Formats crypto values to fixed decimal string."""
    val = decimal.Decimal(str(value))
    return f"{val:.{precision}f}"

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculates percentage change between two price points."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def validate_symbol(symbol: str) -> bool:
    """Checks if crypto symbol format is valid."""
    return bool(symbol and symbol.isalnum() and 2 <= len(symbol) <= 10)

def sanitize_input(value: str) -> str:
    """Removes potential injection characters from inputs."""
    return "".join(char for char in value if char.isalnum())

def get_ticker_pair(base: str, quote: str) -> str:
    """Combines base and quote into standard pair format."""
    return f"{base.upper()}/{quote.upper()}"

def parse_float(value: Union[str, float], default: float = 0.0) -> float:
    """Safely converts value to float with default fallback."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default