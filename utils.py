import time
from decimal import Decimal, ROUND_HALF_UP

def format_currency(value, precision=2):
    """Formats a crypto price to a rounded decimal string."""
    val = Decimal(str(value))
    return str(val.quantize(Decimal('1.' + '0' * precision), rounding=ROUND_HALF_UP))

def get_timestamp():
    """Returns current unix timestamp in milliseconds."""
    return int(time.time() * 1000)

def calculate_percentage_change(current, previous):
    """Calculates percentage change between two values."""
    if not previous or previous == 0:
        return 0.0
    return float(((current - previous) / previous) * 100)

def validate_symbol(symbol):
    """Basic sanitization for cryptocurrency ticker symbols."""
    if not isinstance(symbol, str) or not symbol.isalnum():
        return False
    return symbol.upper().strip()

def retry_operation(func, retries=3, delay=1):
    """Decorator logic for network-based operations with simple retry."""
    for i in range(retries):
        try:
            return func()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay)
            delay *= 2