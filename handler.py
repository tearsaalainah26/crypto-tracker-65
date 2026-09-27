import time
import logging
import requests
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger('crypto-tracker-65')

def retry_request(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    if attempt == retries:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_request(retries=3, delay=2.0)
def fetch_crypto_price(symbol: str) -> dict:
    """Fetches live price data for a given crypto symbol."""
    url = f"https://api.exchange.com/v1/ticker/{symbol}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()