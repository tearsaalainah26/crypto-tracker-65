"""Crypto tracking data validator for main processing pipeline."""

from typing import Any, Dict
import re


class ValidationError(Exception):
    """Raised when incoming market payload fails validation."""
    pass


def validate_symbol(symbol: Any) -> str:
    """Validate and normalize cryptocurrency symbol or ticker pair."""
    if not isinstance(symbol, str):
        raise ValidationError(f"Symbol must be a string, got {type(symbol).__name__}")
    
    clean_symbol = symbol.strip().upper()
    if not re.match(r"^[A-Z0-9]{2,10}(/[A-Z0-9]{2,10})?$", clean_symbol):
        raise ValidationError(f"Invalid crypto symbol format: '{symbol}'")
    
    return clean_symbol


def validate_price(price: Any) -> float:
    """Validate crypto price value to ensure positive numeric entry."""
    try:
        val = float(price)
    except (ValueError, TypeError):
        raise ValidationError(f"Price must be a valid number, got {price!r}")
    
    if val <= 0:
        raise ValidationError(f"Price must be greater than zero, got {val}")
    
    return val


def validate_volume(volume: Any) -> float:
    """Validate trading volume to ensure non-negative value."""
    try:
        val = float(volume)
    except (ValueError, TypeError):
        raise ValidationError(f"Volume must be numeric, got {volume!r}")
    
    if val < 0:
        raise ValidationError(f"Volume cannot be negative, got {val}")
    
    return val


def validate_ticker_payload(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and sanitize raw input data before loop processing."""
    if not isinstance(raw_data, dict):
        raise ValidationError(f"Payload must be a dict, got {type(raw_data).__name__}")

    required_fields = ["symbol", "price", "volume"]
    missing = [field for field in required_fields if field not in raw_data]
    if missing:
        raise ValidationError(f"Missing required ticker payload fields: {', '.join(missing)}")

    return {
        "symbol": validate_symbol(raw_data["symbol"]),
        "price": validate_price(raw_data["price"]),
        "volume": validate_volume(raw_data["volume"]),
        "timestamp": int(raw_data.get("timestamp", 0))
    }
