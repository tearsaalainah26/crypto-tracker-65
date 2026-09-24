import time
import requests
from functools import wraps
from typing import Callable, Any

def with_retry(max_attempts: int = 3, delay: float = 2.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(delay * attempts)
            return None
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1.5)
def fetch_crypto_price(ticker: str) -> float:
    """Fetches live price data from crypto exchange API."""
    url = f"https://api.exchange.com/v1/price/{ticker}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    return float(data.get('price', 0.0))