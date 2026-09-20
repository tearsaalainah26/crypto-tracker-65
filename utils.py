import decimal
from typing import Union

def format_currency(value: Union[float, str, decimal.Decimal], precision: int = 2) -> str:
    """Format crypto values as currency strings."""
    val = decimal.Decimal(str(value))
    return f"${val:,.{precision}f}"

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculate price movement percentage between two values."""
    if old_price == 0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100

def validate_symbol(symbol: str) -> bool:
    """Check if ticker symbol matches standard crypto format."""
    return bool(symbol.isupper() and 2 <= len(symbol) <= 10)

def to_decimal(value: Union[float, str]) -> decimal.Decimal:
    """Convert numeric inputs to fixed-point decimal objects."""
    try:
        return decimal.Decimal(str(value))
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0.0')