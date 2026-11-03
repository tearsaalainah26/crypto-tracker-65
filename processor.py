import math
from typing import Dict, Any, Optional


class CryptoDataProcessingError(Exception):
    """Raised when crypto price processing fails due to unrecoverable edge cases."""
    pass


class MarketProcessor:
    """Processes raw cryptocurrency market data with robust error handling for edge cases."""

    def __init__(self, max_allowed_slippage: float = 0.5):
        self.max_allowed_slippage = max_allowed_slippage

    def calculate_price_change(self, current_price: float, previous_price: float) -> float:
        """Calculate percentage price change safely handling zero or negative values."""
        if not isinstance(current_price, (int, float)) or not isinstance(previous_price, (int, float)):
            raise TypeError("Prices must be numeric values")

        if previous_price <= 0:
            # Edge case: corrupt feed reporting non-positive base price
            return 0.0

        if math.isnan(current_price) or math.isnan(previous_price):
            return 0.0

        return ((current_price - previous_price) / previous_price) * 100.0

    def parse_ticker_payload(self, raw_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Parses raw ticker dictionary, safely extracting required fields while ignoring malformed payloads."""
        if not isinstance(raw_data, dict):
            return None

        symbol = raw_data.get("symbol")
        if not symbol or not isinstance(symbol, str):
            symbol = "UNKNOWN:USD"
        else:
            symbol = symbol.strip().upper()

        try:
            raw_price = raw_data.get("price")
            price = float(raw_price) if raw_price is not None else 0.0
            if price < 0 or math.isinf(price):
                price = 0.0
        except (ValueError, TypeError):
            # Edge case: unparseable string or invalid object passed as price
            price = 0.0

        try:
            raw_volume = raw_data.get("volume_24h", 0.0)
            volume = float(raw_volume) if raw_volume is not None else 0.0
            if volume < 0 or math.isinf(volume):
                volume = 0.0
        except (ValueError, TypeError):
            volume = 0.0

        return {
            "symbol": symbol,
            "price": price,
            "volume_24h": volume,
            "is_stale": bool(raw_data.get("stale", False))
        }
