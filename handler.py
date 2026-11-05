import logging
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


def safe_decimal(val: Any, default: Optional[Decimal] = None) -> Optional[Decimal]:
    """Safely convert arbitrary values to Decimal handling edge case types."""
    if val is None or val == "":
        return default
    try:
        str_val = str(val).strip()
        return Decimal(str_val)
    except (InvalidOperation, ValueError, TypeError) as err:
        logger.warning(f"Failed to convert {val!r} to Decimal: {err}")
        return default


def calculate_price_change(current_price: Any, previous_price: Any) -> Optional[Decimal]:
    """Calculate percentage price change safely handling zero or invalid inputs."""
    curr = safe_decimal(current_price)
    prev = safe_decimal(previous_price)

    if curr is None or prev is None:
        logger.error("Cannot calculate change: missing price data")
        return None

    if prev <= Decimal("0"):
        logger.warning(f"Invalid previous price for calculation: {prev}")
        return None

    try:
        change = ((curr - prev) / prev) * Decimal("100")
        return change.quantize(Decimal("0.01"))
    except Exception as exc:
        logger.error(f"Unexpected error calculating price change: {exc}")
        return None


def extract_ticker_data(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Extract and sanitize crypto ticker payload with edge-case handling."""
    if not isinstance(payload, dict) or not payload:
        logger.warning("Empty or non-dict payload received")
        return {"symbol": "UNKNOWN", "price": None, "volume_24h": None, "valid": False}

    symbol = str(payload.get("symbol", "UNKNOWN")).upper().strip()
    raw_price = payload.get("price") or payload.get("last_price")
    raw_volume = payload.get("volume_24h") or payload.get("vol_24h")

    price = safe_decimal(raw_price)
    volume = safe_decimal(raw_volume)

    is_valid = price is not None and price > Decimal("0") and bool(symbol != "UNKNOWN")

    return {
        "symbol": symbol,
        "price": price,
        "volume_24h": volume if (volume is not None and volume >= Decimal("0")) else Decimal("0"),
        "valid": is_valid,
    }
