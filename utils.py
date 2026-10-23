from datetime import datetime, timezone
from typing import Dict, Any


def normalize_symbol(symbol: str) -> str:
    """Format raw trading symbol into standard uppercase BASE/QUOTE format."""
    clean_symbol = symbol.replace("-", "").replace("_", "").replace("/", "").upper()
    if clean_symbol.endswith("USDT"):
        return f"{clean_symbol[:-4]}/USDT"
    if clean_symbol.endswith("USD"):
        return f"{clean_symbol[:-3]}/USD"
    if clean_symbol.endswith("BTC"):
        return f"{clean_symbol[:-3]}/BTC"
    return clean_symbol


def format_currency(val: float, precision: int = 2) -> str:
    """Format float values as localized currency strings with adaptive precision."""
    if val >= 1.0:
        return f"${val:,.{precision}f}"
    return f"${val:.6f}"


def calculate_price_change(current: float, previous: float) -> Dict[str, Any]:
    """Calculate absolute and percentage change between two price points."""
    if previous <= 0:
        return {"diff": 0.0, "pct_change": 0.0, "is_bullish": False}

    diff = current - previous
    pct_change = (diff / previous) * 100
    return {
        "diff": round(diff, 6),
        "pct_change": round(pct_change, 2),
        "is_bullish": diff >= 0,
    }


def parse_unix_timestamp(ts: int) -> str:
    """Convert unix timestamp in seconds or milliseconds to ISO 8601 string."""
    ts_seconds = ts / 1000.0 if ts > 1e11 else float(ts)
    dt = datetime.fromtimestamp(ts_seconds, tz=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
