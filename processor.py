import math
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class CryptoDataProcessor:
    """Process and validate raw cryptocurrency ticker payloads."""

    REQUIRED_KEYS = {"symbol", "price", "volume", "timestamp"}

    def __init__(self, max_price_threshold: float = 1_000_000.0):
        self.max_price_threshold = max_price_threshold

    def process_ticker(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Clean, validate, and normalize a raw ticker payload.

        Handles edge cases such as null values, non-numeric prices,
        out-of-bound values, and unexpected payload structures.
        """
        if not isinstance(payload, dict):
            logger.warning(f"Invalid payload type: expected dict, got {type(payload).__name__}")
            return None

        missing_keys = self.REQUIRED_KEYS - payload.keys()
        if missing_keys:
            logger.error(f"Payload missing required keys: {missing_keys}")
            return None

        try:
            symbol = str(payload["symbol"]).upper().strip()
            if not symbol or len(symbol) > 12:
                logger.warning(f"Malformed ticker symbol: {payload.get('symbol')}")
                return None

            price = float(payload["price"])
            volume = float(payload["volume"])
            timestamp = int(payload["timestamp"])

            if math.isnan(price) or math.isinf(price) or price <= 0:
                logger.warning(f"Invalid price value for {symbol}: {price}")
                return None

            if math.isnan(volume) or math.isinf(volume) or volume < 0:
                logger.warning(f"Invalid volume value for {symbol}: {volume}")
                return None

            if price > self.max_price_threshold:
                logger.warning(f"Price for {symbol} exceeds threshold: {price}")
                return None

            if timestamp <= 0:
                logger.warning(f"Invalid timestamp for {symbol}: {timestamp}")
                return None

            return {
                "symbol": symbol,
                "price": round(price, 8),
                "volume": round(volume, 4),
                "timestamp": timestamp,
                "is_anomaly": price > 500000.0,
            }

        except (ValueError, TypeError) as err:
            logger.error(f"Failed to parse numeric fields in payload: {err}")
            return None
        except Exception as err:
            logger.error(f"Unexpected error processing ticker payload: {err}")
            return None
