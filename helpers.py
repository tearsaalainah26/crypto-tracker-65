import time
from decimal import Decimal, ROUND_HALF_UP
from typing import Union

def format_currency(value: Union[float, str, Decimal], decimals: int = 2) -> str:
    """Formats numerical values into standard currency strings."""
    d = Decimal(str(value))
    precision = Decimal('0.' + '0' * (decimals - 1) + '1')
    return str(d.quantize(precision, rounding=ROUND_HALF_UP))

def get_timestamp() -> int:
    """Returns current UTC unix timestamp."""
    return int(time.time())

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculates percentage difference between two price points."""
    if old_price == 0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100

def validate_ticker(ticker: str) -> bool:
    """Checks if ticker string follows standard crypto format."""
    if not ticker or not isinstance(ticker, str):
        return False
    return ticker.isalnum() and 1 <= len(ticker) <= 10

def retry_operation(func, retries: int = 3, delay: int = 1):
    """Simple wrapper for retrying network-dependent functions."""
    for i in range(retries):
        try:
            return func()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay)
            delay *= 2