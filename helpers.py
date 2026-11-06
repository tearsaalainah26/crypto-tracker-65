import decimal
from typing import Union

def format_crypto_amount(amount: Union[float, str, decimal.Decimal], precision: int = 8) -> str:
    """Normalize crypto amounts to string with fixed precision."""
    val = decimal.Decimal(str(amount))
    return f"{val:.{precision}f}"

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculate percentage difference between two price points."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def sanitize_symbol(symbol: str) -> str:
    """Ensure symbol is uppercase and strip whitespace."""
    return symbol.strip().upper()

def get_ticker_pair(base: str, quote: str = "USDT") -> str:
    """Combine base and quote currencies into standard format."""
    return f"{sanitize_symbol(base)}/{sanitize_symbol(quote)}"

def is_valid_price(price: float) -> bool:
    """Check if price is a valid positive number."""
    return isinstance(price, (int, float)) and price > 0