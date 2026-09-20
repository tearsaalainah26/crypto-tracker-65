import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("crypto_tracker.processor")

class MarketDataProcessor:
    """Processes incoming cryptocurrency tick and trade data with input validation."""

    def __init__(self, supported_symbols: Optional[List[str]] = None):
        default_symbols = ["BTC", "ETH", "SOL", "ADA", "DOT", "XRP"]
        self.supported_symbols = set(supported_symbols or default_symbols)

    def validate_tick_data(self, data: Dict[str, Any]) -> bool:
        """Validate schema and numerical ranges for market tick data."""
        if not isinstance(data, dict):
            logger.warning("Invalid payload format: expected dict, got %s", type(data).__name__)
            return False

        symbol = data.get("symbol")
        if not isinstance(symbol, str) or symbol.upper() not in self.supported_symbols:
            logger.warning("Validation error: unsupported or missing symbol '%s'", symbol)
            return False

        price = data.get("price")
        if not isinstance(price, (int, float)) or price <= 0:
            logger.warning("Validation error: price must be a positive number, got %s", price)
            return False

        volume = data.get("volume")
        if not isinstance(volume, (int, float)) or volume < 0:
            logger.warning("Validation error: volume must be non-negative, got %s", volume)
            return False

        return True

    def process_stream(self, raw_ticks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop filtering out invalid input records."""
        validated_records = []
        for raw_item in raw_ticks:
            if not self.validate_tick_data(raw_item):
                continue

            # Standardize validated tick format
            clean_tick = {
                "symbol": raw_item["symbol"].upper(),
                "price": float(raw_item["price"]),
                "volume": float(raw_item["volume"]),
                "timestamp": raw_item.get("timestamp")
            }
            validated_records.append(clean_tick)

        logger.info("Processed %d valid records out of %d received", len(validated_records), len(raw_ticks))
        return validated_records
