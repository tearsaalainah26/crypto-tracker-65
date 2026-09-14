import logging
from typing import Optional, Any

logger = logging.getLogger('crypto-tracker-65')

class CryptoError(Exception):
    """Base exception for crypto-tracker-65."""
    pass

def safe_get_price(data: dict, symbol: str) -> Optional[float]:
    """Extracts price from API response with defensive checks."""
    try:
        if not isinstance(data, dict):
            raise ValueError('Invalid data format')
        
        price = data.get('market_data', {}).get(symbol, {}).get('price')
        
        if price is None:
            logger.warning(f'Price data missing for {symbol}')
            return None
            
        return float(price)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f'Data parsing failed for {symbol}: {e}')
        return None

def validate_ticker(ticker: Any) -> str:
    """Validates ticker format before external requests."""
    if not isinstance(ticker, str):
        raise CryptoError('Ticker must be a string')
    
    cleaned = ticker.strip().upper()
    if not cleaned.isalnum():
        raise CryptoError(f'Invalid characters in ticker: {cleaned}')
    
    return cleaned