import time
import functools
import logging
import requests

logger = logging.getLogger('crypto-tracker-65')

def retry_request(max_retries=3, delay=2):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            logger.error(f"All {max_retries} retries failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator

@retry_request(max_retries=3, delay=1)
def fetch_crypto_price(url):
    """Example network call using the retry decorator."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()