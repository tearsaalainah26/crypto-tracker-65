import decimal
from typing import Dict, Any, Optional

def format_crypto_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalizes API response into standard tracking format."""
    try:
        ticker = raw_data.get("symbol", "UNKNOWN").upper()
        price_raw = raw_data.get("price", "0.0")
        volume_raw = raw_data.get("volume_24h", "0.0")

        return {
            "ticker": ticker,
            "price_usd": float(decimal.Decimal(str(price_raw))),
            "volume_24h": float(decimal.Decimal(str(volume_raw))),
            "is_active": raw_data.get("status") == "live"
        }
    except (ValueError, decimal.InvalidOperation):
        return {"error": "invalid numerical format provided"}

def calculate_percent_change(current: float, previous: float) -> Optional[float]:
    """Calculates price variance percentage between intervals."""
    if previous == 0:
        return None
    
    diff = current - previous
    return round((diff / previous) * 100, 4)

def sanitize_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Strips empty values from incoming socket streams."""
    return {k: v for k, v in data.items() if v is not None}