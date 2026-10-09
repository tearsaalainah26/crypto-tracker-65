import re
from typing import Any, Dict


def validate_symbol(symbol: str) -> str:
    """Validate and normalize a cryptocurrency trading pair symbol."""
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string")
    cleaned = symbol.strip().upper()
    pattern = r"^[A-Z0-9]{2,10}(?:[/\-_][A-Z0-9]{2,10})?$"
    if not re.match(pattern, cleaned):
        raise ValueError(f"Invalid crypto symbol format: '{symbol}'")
    return cleaned


def validate_numeric_value(val: Any, field_name: str, allow_zero: bool = False) -> float:
    """Validate and convert numeric input values like price or volume."""
    try:
        num = float(val)
    except (TypeError, ValueError):
        raise ValueError(f"Field '{field_name}' must be a valid number, got '{val}'")
    
    if allow_zero and num < 0:
        raise ValueError(f"Field '{field_name}' cannot be negative")
    elif not allow_zero and num <= 0:
        raise ValueError(f"Field '{field_name}' must be greater than zero")
    return num


def validate_crypto_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate raw incoming market data payload before processing."""
    if not isinstance(payload, dict):
        raise ValueError("Input payload must be a dictionary")

    required_keys = ["symbol", "price", "volume"]
    missing = [key for key in required_keys if key not in payload]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    return {
        "symbol": validate_symbol(payload["symbol"]),
        "price": validate_numeric_value(payload["price"], "price", allow_zero=False),
        "volume": validate_numeric_value(payload["volume"], "volume", allow_zero=True),
        "timestamp": payload.get("timestamp"),
    }
