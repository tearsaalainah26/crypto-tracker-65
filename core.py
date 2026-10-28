from typing import Any, Dict, List, Optional


def calculate_vwap(trades: List[Dict[str, float]]) -> Optional[float]:
    """Calculate Volume-Weighted Average Price (VWAP) from trade execution records."""
    if not trades:
        return None

    total_volume = sum(trade.get("volume", 0.0) for trade in trades)
    if total_volume <= 0:
        return None

    total_pv = sum(
        trade.get("price", 0.0) * trade.get("volume", 0.0) for trade in trades
    )
    return round(total_pv / total_volume, 8)


def normalize_ticker_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize multi-exchange raw ticker payload into standard layout."""
    symbol = str(raw_data.get("symbol", "")).upper().replace("-", "").replace("_", "")
    last_price = float(raw_data.get("last_price", raw_data.get("price", 0.0)))
    volume_24h = float(raw_data.get("volume_24h", raw_data.get("volume", 0.0)))
    high_24h = float(raw_data.get("high_24h", raw_data.get("high", last_price)))
    low_24h = float(raw_data.get("low_24h", raw_data.get("low", last_price)))

    open_price = float(raw_data.get("open_price", raw_data.get("open", 0.0)))
    price_change_pct = 0.0
    if open_price > 0:
        price_change_pct = round(((last_price - open_price) / open_price) * 100, 2)

    return {
        "symbol": symbol,
        "last_price": last_price,
        "open_price": open_price,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "volume_24h": volume_24h,
        "price_change_pct_24h": price_change_pct,
    }


def format_market_cap(usd_value: float) -> str:
    """Format large USD market cap values into human-readable strings."""
    if usd_value >= 1e12:
        return f"${usd_value / 1e12:.2f}T"
    if usd_value >= 1e9:
        return f"${usd_value / 1e9:.2f}B"
    if usd_value >= 1e6:
        return f"${usd_value / 1e6:.2f}M"
    if usd_value >= 1e3:
        return f"${usd_value / 1e3:.2f}K"
    return f"${usd_value:.2f}"
