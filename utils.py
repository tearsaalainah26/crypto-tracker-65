from typing import Dict, Any, Optional
from decimal import Decimal, InvalidOperation


def format_currency(value: float | Decimal, precision: int = 2) -> str:
    """Format a numeric value into a standardized currency string."""
    try:
        dec_val = Decimal(str(value))
        return f"${dec_val:,.{precision}f}"
    except (InvalidOperation, TypeError):
        return "$0.00"


def normalize_ticker_data(raw_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Extract and normalize standard crypto ticker attributes from raw API payload."""
    if not isinstance(raw_data, dict):
        return None

    symbol = raw_data.get("symbol") or raw_data.get("pair") or raw_data.get("ticker")
    price = raw_data.get("price") or raw_data.get("last_price") or raw_data.get("last")
    volume = raw_data.get("volume") or raw_data.get("base_volume") or raw_data.get("vol_24h")
    change_24h = raw_data.get("change_24h") or raw_data.get("priceChangePercent") or 0.0

    if not symbol or price is None:
        return None

    try:
        parsed_price = float(price)
        parsed_vol = float(volume) if volume else 0.0
        parsed_change = float(change_24h)
    except (ValueError, TypeError):
        return None

    return {
        "symbol": str(symbol).upper(),
        "price": parsed_price,
        "formatted_price": format_currency(parsed_price, precision=4 if parsed_price < 1.0 else 2),
        "volume_24h": parsed_vol,
        "change_24h": parsed_change,
        "is_bullish": parsed_change >= 0,
    }


def calculate_price_impact(order_amount: float, order_book_depth: float) -> float:
    """Calculate estimated price impact percentage for a market order based on liquidity."""
    if order_book_depth <= 0 or order_amount <= 0:
        return 0.0
    impact = (order_amount / order_book_depth) * 100
    return round(min(impact, 100.0), 2)
