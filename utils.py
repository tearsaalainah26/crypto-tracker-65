from typing import Dict, Any, Optional
from datetime import datetime

def format_crypto_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Parses raw API response into standardized application format."""
    try:
        return {
            "symbol": raw_data.get("symbol", "UNKNOWN").upper(),
            "price_usd": float(raw_data.get("price", 0.0)),
            "timestamp": datetime.utcnow().isoformat(),
            "market_cap": float(raw_data.get("market_cap", 0.0)),
            "is_active": raw_data.get("status") == "active"
        }
    except (ValueError, TypeError, AttributeError):
        return {}

def calculate_portfolio_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Calculates total value based on asset holdings and current prices."""
    total = 0.0
    for asset, quantity in holdings.items():
        price = prices.get(asset, 0.0)
        total += quantity * price
    return round(total, 2)

def validate_ticker(ticker: str) -> bool:
    """Checks if the provided ticker string matches standard crypto formats."""
    if not isinstance(ticker, str):
        return False
    return 2 <= len(ticker) <= 10 and ticker.isalnum()