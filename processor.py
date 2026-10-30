import decimal
from typing import Dict, Union

def format_currency(value: Union[float, str, decimal.Decimal], symbol: str = 'USD') -> str:
    """Formats crypto price with two decimal precision."""
    val = decimal.Decimal(str(value))
    return f"{symbol} {val:,.2f}"

def calculate_portfolio_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Computes total value of assets in holdings."""
    total = 0.0
    for asset, amount in holdings.items():
        price = prices.get(asset, 0.0)
        total += amount * price
    return round(total, 2)

def sanitize_symbol(symbol: str) -> str:
    """Standardizes ticker symbols to uppercase."""
    return symbol.strip().upper()

def get_percentage_change(current: float, previous: float) -> float:
    """Calculates percentage difference between two prices."""
    if previous == 0:
        return 0.0
    return round(((current - previous) / previous) * 100, 2)