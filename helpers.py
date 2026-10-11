import decimal
from typing import Union

def format_currency(value: Union[float, str, decimal.Decimal], precision: int = 2) -> str:
    """Formats crypto values to human-readable string."""
    d = decimal.Decimal(str(value))
    return f"{d:,.{precision}f}"

def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculates percentage change between two values."""
    if old_value == 0:
        return 0.0
    return ((new_value - old_value) / old_value) * 100

def validate_symbol(symbol: str) -> bool:
    """Checks if symbol string follows standard crypto format."""
    return bool(symbol and symbol.isalnum() and len(symbol) <= 10)

def sanitize_price_data(raw_data: dict) -> dict:
    """Cleans raw API response dictionary."""
    return {
        "price": float(raw_data.get("price_usd", 0)),
        "symbol": str(raw_data.get("symbol", "UNKNOWN")).upper(),
        "timestamp": raw_data.get("last_updated", 0)
    }