import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("crypto_tracker.processor")

class ProcessingError(Exception):
    """Custom exception for crypto data processing errors."""
    pass

class CryptoDataProcessor:
    """Processes raw cryptocurrency market data with robust edge-case handling."""

    def __init__(self, decimal_places: int = 2):
        self.decimal_places = decimal_places

    def calculate_price_change(self, current_price: float, previous_price: float) -> float:
        """Calculates percentage change, handling division by zero and negative values."""
        if previous_price <= 0:
            logger.warning(f"Invalid previous price {previous_price} for change calculation. Defaulting to 0.0.")
            return 0.0
        if current_price < 0:
            logger.warning(f"Negative current price {current_price} encountered. Defaulting to 0.0.")
            current_price = 0.0
            
        change = ((current_price - previous_price) / previous_price) * 100
        return round(change, self.decimal_places)

    def process_ticker_payload(self, payload: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Parses raw ticker payload, gracefully handling missing keys or bad types."""
        if not payload:
            raise ProcessingError("Payload is empty or None")

        symbol = payload.get("symbol")
        if not isinstance(symbol, str) or not symbol.strip():
            raise ProcessingError("Missing or invalid symbol in ticker payload")

        try:
            current_price = float(payload.get("price", 0.0))
            previous_price = float(payload.get("prev_price", 0.0))
            volume = float(payload.get("volume24h", 0.0))
        except (ValueError, TypeError) as err:
            raise ProcessingError(f"Malformed numeric values in payload: {err}")

        price_change_pct = self.calculate_price_change(current_price, previous_price)

        return {
            "symbol": symbol.strip().upper(),
            "price": max(0.0, current_price),
            "price_change_pct": price_change_pct,
            "volume_positive": volume > 0,
            "volume": max(0.0, volume)
        }