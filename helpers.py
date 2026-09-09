import math
from typing import Union


def format_currency(value: Union[int, float], symbol: str = "$") -> str:
    """Formats a numeric value as a currency string with appropriate decimals."""
    if value is None:
        return f"{symbol}0.00"
    if abs(value) >= 1.0:
        return f"{symbol}{value:,.2f}"
    if value == 0:
        return f"{symbol}0.00"
    # For small crypto prices, show up to 8 decimal places
    decimals = max(2, min(8, -int(math.floor(math.log10(abs(value)))) + 1))
    return f"{symbol}{value:,.{decimals}f}"


def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculates the percentage change between two prices."""
    if not old_price:
        return 0.0
    return ((new_price - old_price) / old_price) * 100.0


def validate_ticker(ticker: str) -> bool:
    """Validates if a ticker symbol is in a correct format."""
    if not ticker or not isinstance(ticker, str):
        return False
    clean_ticker = ticker.strip().upper()
    return clean_ticker.isalnum() and 2 <= len(clean_ticker) <= 10
