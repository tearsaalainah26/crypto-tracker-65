import logging
from typing import Optional, Any

logger = logging.getLogger(__name__)

class CryptoDataError(Exception):
    """Base exception for crypto-tracker-65 data operations."""
    pass

def safe_get_price(data: dict, symbol: str) -> Optional[float]:
    """Extracts price with validation and error logging."""
    try:
        if not isinstance(data, dict):
            raise ValueError("Response data must be a dictionary")
        
        price = data.get('quotes', {}).get(symbol, {}).get('price')
        
        if price is None:
            logger.warning(f"Price not found for {symbol}")
            return None
            
        return float(price)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Data parsing error for {symbol}: {str(e)}")
        return None

def validate_api_response(response: Any) -> bool:
    """Ensures API response matches expected structure."""
    if response is None:
        return False
    try:
        return 'status' in response and response['status'].get('error_code') == 0
    except Exception as e:
        logger.critical(f"Malformed API response structure: {str(e)}")
        return False