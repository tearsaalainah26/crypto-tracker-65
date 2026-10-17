"""Crypto price and ticker data processor with resilient edge-case handling."""

import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


class ProcessingError(Exception):
    """Custom exception for crypto data processing failures."""
    pass


def clean_ticker_price(val: Any) -> Optional[float]:
    """Convert raw price input to float, handling nulls, strings, and invalid values."""
    if val is None:
        return None
    try:
        parsed = float(val)
        if parsed < 0:
            logger.warning(f"Negative price encountered: {parsed}")
            return None
        return parsed
    except (ValueError, TypeError):
        logger.error(f"Failed to parse price value: {val}")
        return None


def process_ticker_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract and normalize crypto ticker data safely.
    
    Handles malformed dicts, missing keys, and bad numeric formats.
    """
    if not isinstance(data, dict) or not data:
        raise ProcessingError("Invalid or empty raw ticker payload")

    symbol = str(data.get("symbol", "")).upper().strip()
    if not symbol:
        raise ProcessingError("Missing symbol in ticker data")

    raw_price = data.get("price") or data.get("lastPrice") or data.get("current_price")
    price = clean_ticker_price(raw_price)
    if price is None:
        logger.warning(f"Unprocessable or missing price for symbol: {symbol}")

    raw_volume = data.get("volume") or data.get("total_volume") or 0.0
    try:
        volume = max(0.0, float(raw_volume))
    except (ValueError, TypeError):
        volume = 0.0

    return {
        "symbol": symbol,
        "price": price,
        "volume_24h": volume,
        "is_valid": price is not None and price > 0,
    }


def batch_process_tickers(payload: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process multiple tickers safely, filtering out completely invalid records."""
    if not isinstance(payload, list):
        logger.error("Batch payload is not a list")
        return []

    results = []
    for item in payload:
        try:
            processed = process_ticker_data(item)
            results.append(processed)
        except ProcessingError as err:
            logger.debug(f"Skipping malformed ticker record: {err}")
        except Exception as err:
            logger.error(f"Unexpected error processing item {item}: {err}")

    return results
