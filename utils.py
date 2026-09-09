import time
import functools
import requests
from typing import Callable, Any

def retry_network_request(max_retries: int = 3, delay: float = 2.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_network_request(max_retries=3, delay=1.0)
def fetch_crypto_price(ticker: str) -> float:
    """Example function for fetching crypto data from an endpoint."""
    url = f"https://api.crypto-tracker-65.com/price/{ticker}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return float(response.json().get("price", 0.0))