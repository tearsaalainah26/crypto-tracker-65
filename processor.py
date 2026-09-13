import logging
import re
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

ALLOWED_TIMEFRAMES = {"1m", "5m", "15m", "1h", "4h", "1d"}
SYMBOL_PATTERN = re.compile(r"^[A-Z0-9]{2,10}-[A-Z0-9]{2,10}$")


def validate_crypto_input(payload: Dict[str, Any]) -> bool:
    """Validate incoming crypto tracking payload structure and values."""
    symbol = payload.get("symbol")
    if not symbol or not isinstance(symbol, str) or not SYMBOL_PATTERN.match(symbol):
        logger.warning(f"Invalid symbol format: {symbol}")
        return False

    price = payload.get("price")
    if not isinstance(price, (int, float)) or price <= 0:
        logger.warning(f"Invalid price for {symbol}: {price}")
        return False

    volume = payload.get("volume")
    if not isinstance(volume, (int, float)) or volume < 0:
        logger.warning(f"Invalid volume for {symbol}: {volume}")
        return False

    timeframe = payload.get("timeframe", "1m")
    if timeframe not in ALLOWED_TIMEFRAMES:
        logger.warning(f"Unsupported timeframe for {symbol}: {timeframe}")
        return False

    return True


def process_market_updates(raw_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Main processing loop that validates and transforms raw market data events."""
    processed_data = []

    for index, event in enumerate(raw_events):
        if not isinstance(event, dict):
            logger.error(f"Skipping non-dict payload at index {index}")
            continue

        if not validate_crypto_input(event):
            logger.error(f"Validation failed for update at index {index}")
            continue

        sanitized_record = {
            "symbol": event["symbol"].upper(),
            "price": float(event["price"]),
            "volume": float(event["volume"]),
            "timeframe": event.get("timeframe", "1m"),
        }
        processed_data.append(sanitized_record)

    return processed_data
