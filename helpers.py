import time
from decimal import Decimal
from typing import Union

def format_currency(value: Union[float, Decimal, str], precision: int = 2) -> str:
    """Converts numeric input to a formatted currency string."""
    val = Decimal(str(value))
    return f"${val:,.{precision}f}"

def get_timestamp() -> int:
    """Returns current UTC unix timestamp."""
    return int(time.time())

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculates percentage difference between two values."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def validate_ticker(ticker: str) -> bool:
    """Checks if ticker format is valid uppercase alphanumeric."""
    return bool(ticker and ticker.isalnum() and ticker.isupper())