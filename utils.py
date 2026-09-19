from typing import Dict, Any, Optional
from decimal import Decimal, InvalidOperation

def format_crypto_price(price: Any, currency: str = 'USD') -> str:
    """Format raw crypto data into a user-friendly string."""
    try:
        value = Decimal(str(price))
        return f"{value:,.2f} {currency.upper()}"
    except (InvalidOperation, ValueError):
        return f"N/A {currency.upper()}"

def calculate_portfolio_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Calculate total value of holdings based on current market prices."""
    total = 0.0
    for asset, amount in holdings.items():
        price = prices.get(asset, 0.0)
        total += amount * price
    return round(total, 2)

def sanitize_asset_symbol(symbol: Optional[str]) -> str:
    """Normalize cryptocurrency symbols to uppercase."""
    if not symbol or not isinstance(symbol, str):
        return "UNKNOWN"
    return symbol.strip().upper()

def get_percentage_change(current: float, previous: float) -> float:
    """Determine the percentage difference between two values."""
    if previous == 0:
        return 0.0
    return round(((current - previous) / previous) * 100, 2)