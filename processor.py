import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class ProcessingError(Exception):
    """Raised when payload validation or processing fails."""
    pass


def validate_crypto_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate incoming cryptocurrency tracking payload."""
    if not isinstance(data, dict):
        raise ProcessingError("Payload must be a dictionary")

    symbol = data.get("symbol")
    if not symbol or not isinstance(symbol, str) or len(symbol) > 10:
        raise ProcessingError("Invalid or missing 'symbol' field")

    price = data.get("price")
    if price is None or not isinstance(price, (int, float)) or price < 0:
        raise ProcessingError("Invalid or missing 'price' value")

    volume = data.get("volume", 0.0)
    if not isinstance(volume, (int, float)) or volume < 0:
        raise ProcessingError("Invalid 'volume' value")

    return {
        "symbol": symbol.upper().strip(),
        "price": float(price),
        "volume": float(volume),
        "timestamp": data.get("timestamp")
    }


def process_incoming_queue(raw_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process a batch of crypto data payloads with input validation."""
    valid_records = []

    for idx, item in enumerate(raw_items):
        try:
            cleaned_data = validate_crypto_payload(item)
            valid_records.append(cleaned_data)
            logger.debug(f"Successfully validated item {idx}: {cleaned_data['symbol']}")
        except ProcessingError as err:
            logger.warning(f"Skipping invalid item at index {idx}: {err}")
        except Exception as err:
            logger.error(f"Unexpected error validating item {idx}: {err}")

    return valid_records
