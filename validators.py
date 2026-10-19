import logging
from typing import Any, Optional

logger = logging.getLogger('crypto-tracker-65')

class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass

def validate_price(price: Any) -> float:
    """Ensures price is a positive numeric value."""
    try:
        val = float(price)
        if val <= 0:
            raise ValidationError(f"Price must be positive, got {val}")
        return val
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid price format received: {price}")
        raise ValidationError(f"Price input must be numeric: {e}")

def validate_ticker(ticker: Any) -> str:
    """Validates that the ticker symbol is a string and non-empty."""
    if not isinstance(ticker, str) or not ticker.strip():
        logger.warning(f"Invalid ticker format attempt: {ticker}")
        raise ValidationError("Ticker symbol must be a non-empty string")
    return ticker.strip().upper()

def validate_market_data(data: Optional[dict]) -> bool:
    """Checks market data integrity before processing."""
    if not data or not isinstance(data, dict):
        return False
    
    required_keys = {'symbol', 'price', 'volume'}
    if not required_keys.issubset(data.keys()):
        logger.debug(f"Incomplete market data payload: {data.keys()}")
        return False
        
    return True