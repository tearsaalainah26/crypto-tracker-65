"""Utility functions for crypto data transformation and formatting."""

from typing import Dict, Any


def normalize_ticker(symbol: str) -> str:
    """Standardize cryptocurrency ticker symbols to uppercase base format."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    return symbol.strip().upper().replace("-", "").replace("_", "")


def calculate_price_change(
    current_price: float, previous_price: float
) -> Dict[str, Any]:
    """Calculate absolute and percentage price change between two points."""
    if previous_price <= 0:
        raise ValueError("Previous price must be greater than zero")

    difference = current_price - previous_price
    percentage = (difference / previous_price) * 100

    return {
        "raw_change": round(difference, 8),
        "percentage_change": round(percentage, 2),
        "is_bullish": difference >= 0,
    }


def format_crypto_amount(
    amount: float, symbol: str = "USD", include_symbol: bool = True
) -> str:
    """Format raw balance or market cap numbers into human-readable strings."""
    if amount >= 1_000_000_000:
        formatted = f"{amount / 1_000_000_000:.2f}B"
    elif amount >= 1_000_000:
        formatted = f"{amount / 1_000_000:.2f}M"
    elif amount >= 1.0:
        formatted = f"{amount:,.2f}"
    else:
        formatted = f"{amount:.6f}"

    if include_symbol:
        return f"{formatted} {symbol.upper()}"
    return formatted
