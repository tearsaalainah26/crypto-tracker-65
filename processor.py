import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

def process_crypto_data(data: Optional[Dict[str, Any]]) -> Optional[float]:
    """Extracts price from raw payload with safety checks."""
    if not data:
        logger.error("Empty payload received for processing")
        return None

    try:
        ticker = data.get('ticker')
        price = data.get('price')

        if ticker is None or price is None:
            raise ValueError(f"Missing required fields in payload: {data.keys()}")

        processed_price = float(price)
        if processed_price < 0:
            raise ValueError(f"Negative price detected: {processed_price}")

        return processed_price

    except (ValueError, TypeError) as e:
        logger.warning(f"Data validation failure: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected error during crypto processing: {e}")
        return None

def batch_process(items: list) -> list:
    """Process list of items with individual error handling."""
    results = []
    for item in items:
        result = process_crypto_data(item)
        if result is not None:
            results.append(result)
    return results