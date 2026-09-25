import time
from typing import Dict, Any, Tuple, Optional, List

def validate_crypto_payload(data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """
    Validates incoming cryptocurrency market data payloads.
    Returns a tuple containing (is_valid, error_message).
    """
    if not isinstance(data, dict):
        return False, "Payload must be a dictionary"

    required_keys = {"symbol", "price", "volume", "timestamp"}
    missing_keys = required_keys - data.keys()
    if missing_keys:
        return False, f"Missing required fields: {', '.join(missing_keys)}"

    # Validate symbol format (e.g., BTC, ETH, SOL)
    symbol = data["symbol"]
    if not isinstance(symbol, str) or not (2 <= len(symbol) <= 10):
        return False, f"Invalid symbol '{symbol}': must be 2-10 characters"
    if not symbol.isalnum():
        return False, f"Invalid symbol '{symbol}': must be alphanumeric"

    # Validate numeric price
    try:
        price = float(data["price"])
        if price <= 0:
            return False, f"Invalid price {price}: must be greater than zero"
    except (ValueError, TypeError):
        return False, "Price must be a valid decimal number"

    # Validate numeric volume
    try:
        volume = float(data["volume"])
        if volume < 0:
            return False, f"Invalid volume {volume}: cannot be negative"
    except (ValueError, TypeError):
        return False, "Volume must be a valid decimal number"

    # Validate reasonable epoch timestamp (within 24 hours of current time)
    try:
        timestamp = float(data["timestamp"])
        current_time = time.time()
        one_day = 86400
        if not (current_time - one_day <= timestamp <= current_time + one_day):
            return False, f"Timestamp {timestamp} is out of realistic sync bounds"
    except (ValueError, TypeError):
        return False, "Timestamp must be a valid Unix epoch timestamp"

    return True, None

def filter_invalid_payloads(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filters and normalizes a batch of cryptocurrency payloads, skipping invalid entries.
    """
    valid_records = []
    for item in batch:
        is_valid, error = validate_crypto_payload(item)
        if is_valid:
            valid_records.append({
                "symbol": str(item["symbol"]).upper(),
                "price": float(item["price"]),
                "volume": float(item["volume"]),
                "timestamp": int(item["timestamp"])
            })
    return valid_records