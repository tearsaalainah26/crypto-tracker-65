import json
from typing import Dict, Any, Optional

def format_crypto_data(data: Dict[str, Any], currency: str = 'USD') -> Dict[str, Any]:
    """
    standardizes incoming crypto API responses into a 
    uniform application schema for crypto-tracker-65.
    """
    try:
        base_info = {
            "symbol": data.get("symbol", "UNKNOWN").upper(),
            "price": float(data.get("price_usd", 0.0)),
            "volume_24h": float(data.get("volume_24h", 0.0)),
            "market_cap": float(data.get("market_cap", 0.0)),
            "currency": currency
        }
        return base_info
    except (ValueError, TypeError) as e:
        return {"error": "data parsing failure", "details": str(e)}

def calculate_percentage_change(current: float, previous: float) -> float:
    """
    computes the percentage change between two price points.
    returns 0.0 if previous price is zero.
    """
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def validate_ticker(ticker: str) -> bool:
    """
    ensures ticker format conforms to crypto standards.
    """
    return isinstance(ticker, str) and 2 <= len(ticker) <= 10