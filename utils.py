import time
import functools
import requests
from typing import Callable, Any

def with_retry(max_attempts: int = 3, delay: float = 2.0):
    """
    Decorator for retrying network operations on failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (attempt + 1))
                        continue
            raise last_exception
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1.0)
def fetch_crypto_price(url: str) -> dict:
    """
    Example network call to fetch price data.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()