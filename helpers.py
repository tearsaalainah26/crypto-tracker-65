"""Utility functions for formatting and calculating cryptocurrency market data."""

from typing import Dict, List, Optional, Union


def format_currency(value: Union[int, float], currency_symbol: str = "$") -> str:
    """Format numerical value into readable currency string with smart precision."""
    if value is None:
        return "N/A"
    
    abs_val = abs(value)
    if abs_val >= 1_000_000_000:
        return f"{currency_symbol}{value / 1_000_000_000:.2f}B"
    elif abs_val >= 1_000_000:
        return f"{currency_symbol}{value / 1_000_000:.2f}M"
    elif abs_val >= 1_000:
        return f"{currency_symbol}{value:,.2f}"
    elif abs_val < 0.01:
        return f"{currency_symbol}{value:.6f}"
    else:
        return f"{currency_symbol}{value:.2f}"


def calculate_price_change(current_price: float, past_price: float) -> Optional[float]:
    """Calculate percentage price change between two price points."""
    if not past_price or past_price <= 0:
        return None
    return ((current_price - past_price) / past_price) * 100.0


def normalize_ticker(symbol: str) -> str:
    """Sanitize and standardize crypto ticker symbol format."""
    if not symbol:
        return ""
    cleaned = symbol.strip().upper().replace("/", "").replace("-", "")
    return cleaned


def calculate_simple_moving_average(prices: List[float], period: int = 14) -> List[Optional[float]]:
    """Calculate Simple Moving Average (SMA) over a list of historical prices."""
    if len(prices) < period or period <= 0:
        return [None] * len(prices)

    sma_values: List[Optional[float]] = [None] * (period - 1)
    for i in range(period - 1, len(prices)):
        window = prices[i - period + 1 : i + 1]
        sma_values.append(sum(window) / period)

    return sma_values
