import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def validate_payload(data: Dict[str, Any]) -> bool:
    """Validate standard crypto ticker payload fields and types."""
    if not isinstance(data, dict):
        return False

    required_keys = {"symbol", "price", "volume", "timestamp"}
    if not required_keys.issubset(data.keys()):
        return False

    symbol = data.get("symbol")
    if not isinstance(symbol, str) or len(symbol.strip()) < 3:
        return False

    try:
        price = float(data["price"])
        volume = float(data["volume"])
        timestamp = int(data["timestamp"])
        if price <= 0 or volume < 0 or timestamp <= 0:
            return False
    except (ValueError, TypeError):
        return False

    return True


def process_ticker_batch(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process stream batch with strict record validation in main loop."""
    valid_records = []

    for record in batch:
        if not validate_payload(record):
            logger.warning(f"Invalid record skipped: {record}")
            continue

        clean_data = {
            "symbol": str(record["symbol"]).upper().strip(),
            "price": round(float(record["price"]), 8),
            "volume": round(float(record["volume"]), 4),
            "timestamp": int(record["timestamp"]),
        }
        valid_records.append(clean_data)

    return valid_records
