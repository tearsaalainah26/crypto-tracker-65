import math
from typing import List, Dict, Optional


def format_crypto_price(price: float, currency_symbol: str = "$") -> str:
    """Format a cryptocurrency price with appropriate decimal precision."""
    if price is None:
        return f"{currency_symbol}0.00"
    if price >= 1.0:
        return f"{currency_symbol}{price:,.2f}"
    elif price >= 0.0001:
        return f"{currency_symbol}{price:,.4f}"
    else:
        return f"{currency_symbol}{price:,.8f}"


def calculate_price_change(current: float, previous: float) -> Dict[str, float]:
    """Calculate absolute and percentage price change between two points."""
    if not previous or previous == 0:
        return {"absolute": 0.0, "percentage": 0.0}

    diff = current - previous
    percentage = (diff / previous) * 100.0
    return {"absolute": round(diff, 8), "percentage": round(percentage, 2)}


def normalize_ticker_symbol(symbol: str) -> str:
    """Clean and normalize cryptocurrency ticker symbols."""
    if not symbol:
        return ""
    cleaned = symbol.strip().upper()
    for delimiter in ["/", "-", "_", " "]:
        cleaned = cleaned.replace(delimiter, "")
    return cleaned


def calculate_simple_moving_average(prices: List[float], period: int) -> Optional[float]:
    """Calculate the Simple Moving Average (SMA) for closing prices."""
    if not prices or len(prices) < period or period <= 0:
        return None
    recent_prices = prices[-period:]
    return round(sum(recent_prices) / period, 8)
