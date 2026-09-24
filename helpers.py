import logging
import requests
from requests.exceptions import RequestException, Timeout

logger = logging.getLogger('crypto-tracker-65')

def fetch_crypto_price(symbol: str) -> float:
    """Fetches current market price with resilience."""
    url = f"https://api.exchange.com/v1/ticker/{symbol}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if 'price' not in data:
            raise ValueError(f"Invalid API response structure for {symbol}")
            
        return float(data['price'])

    except Timeout:
        logger.error(f"Network timeout while fetching {symbol}")
        return 0.0
    except RequestException as e:
        logger.error(f"Network error for {symbol}: {e}")
        return 0.0
    except (ValueError, TypeError, KeyError) as e:
        logger.error(f"Data parsing failure for {symbol}: {e}")
        return 0.0

def sanitize_input(symbol: str) -> str:
    """Ensures crypto ticker is safe for API requests."""
    if not symbol or not isinstance(symbol, str):
        return "BTC"
    
    clean = symbol.strip().upper()
    if not clean.isalnum():
        logger.warning(f"Invalid characters in ticker: {clean}")
        return "BTC"
        
    return clean