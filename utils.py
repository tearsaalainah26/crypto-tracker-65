import time
import decimal
from typing import Union

def format_currency(value: Union[float, str, decimal.Decimal], precision: int = 8) -> str:
    """Format crypto values to a consistent decimal string."""
    val = decimal.Decimal(str(value))
    return f"{val:.{precision}f}".rstrip('0').rstrip('.')

def get_timestamp() -> int:
    """Return current Unix epoch time."""
    return int(time.time())

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculate price percentage movement."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def retry_operation(func, retries: int = 3, delay: int = 2):
    """Execute function with simple retry logic."""
    last_ex = None
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            last_ex = e
            time.sleep(delay)
    raise last_ex