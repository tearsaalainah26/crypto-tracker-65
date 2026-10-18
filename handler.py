import logging
import time
from typing import Any, Dict, Optional, Union

logger = logging.getLogger(__name__)


class CryptoAPIError(Exception):
    """Base exception for cryptocurrency API communication failures."""

    pass


class InvalidSymbolError(CryptoAPIError):
    """Raised when an invalid or unsupported symbol is requested."""

    pass


def parse_ticker_response(
    raw_data: Optional[Dict[str, Any]], symbol: str
) -> Dict[str, Union[str, float, int]]:
    """Extracts price and market data from raw crypto provider responses.

    Handles missing keys, unexpected payloads, and edge-case errors.
    """
    if raw_data is None:
        logger.error("Received empty payload for symbol: %s", symbol)
        raise CryptoAPIError(f"API returned empty response for '{symbol}'")

    if not isinstance(raw_data, dict):
        logger.error("Invalid payload type for %s: expected dict", symbol)
        raise CryptoAPIError("Malformed JSON response from data provider")

    if "error" in raw_data or "message" in raw_data:
        err_msg = str(raw_data.get("error") or raw_data.get("message"))
        if "not found" in err_msg.lower() or "invalid" in err_msg.lower():
            raise InvalidSymbolError(f"Cryptocurrency symbol '{symbol}' not found")
        raise CryptoAPIError(f"Provider error: {err_msg}")

    payload = raw_data.get("data", raw_data)

    try:
        price = float(payload["price"])
        volume = float(payload.get("volume_24h", 0.0))
        change = float(payload.get("change_24h", 0.0))
    except (KeyError, TypeError, ValueError) as err:
        logger.warning("Failed parsing numerical fields for %s: %s", symbol, err)
        raise CryptoAPIError(
            f"Incomplete or corrupt market data for symbol '{symbol}'"
        ) from err

    if price <= 0:
        logger.warning("Non-positive price anomaly detected for %s: %f", symbol, price)

    return {
        "symbol": symbol.upper(),
        "price": price,
        "volume_24h": volume,
        "change_24h": change,
        "timestamp": int(time.time()),
    }
