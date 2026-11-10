import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

def process_price_data(data: Optional[Dict[str, Any]]) -> Optional[float]:
    """Extracts price from raw payload with robust error handling."""
    try:
        if not isinstance(data, dict):
            raise ValueError("Invalid payload format: dictionary expected")
        
        price_val = data.get("price")
        if price_val is None:
            raise KeyError("Missing mandatory price field in payload")
        
        float_price = float(price_val)
        if float_price < 0:
            raise ValueError(f"Negative price detected: {float_price}")
            
        return float_price

    except (ValueError, TypeError) as e:
        logger.error(f"Data transformation error: {e}")
        return None
    except KeyError as e:
        logger.warning(f"Schema validation failure: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected processor failure: {e}")
        return None

def validate_ticker(ticker: Any) -> str:
    """Sanitizes and validates crypto ticker strings."""
    if not isinstance(ticker, str) or not ticker.isalnum():
        raise ValueError("Invalid ticker format encountered")
    return ticker.upper().strip()