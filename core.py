import time
import logging
import requests
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger('crypto-tracker-65')

def retry_request(max_retries: int = 3, delay: int = 2):
    """Decorator to retry network requests on failure."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            logger.error(f"Failed after {max_retries} attempts: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

@retry_request(max_retries=3, delay=5)
def fetch_price(symbol: str) -> float:
    """Fetch current price for a crypto asset."""
    url = f"https://api.crypto-tracker.com/v1/ticker/{symbol}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return float(data['price'])

if __name__ == "__main__":
    # Example usage for tracker core
    try:
        btc_price = fetch_price("BTC")
        print(f"Current BTC Price: {btc_price}")
    except Exception as e:
        print(f"Operation failed: {e}")