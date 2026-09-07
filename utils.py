import time
import logging
import functools
import requests

logger = logging.getLogger(__name__)

def retry_network_op(max_retries: int = 3, backoff_factor: float = 1.0, exceptions=(requests.RequestException,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            delay = backoff_factor
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(f"Failed {func.__name__} after {max_retries} attempts: {exc}")
                        raise
                    logger.warning(
                        f"Network operation {func.__name__} failed ({exc}). Retrying in {delay:.2f}s... ({retries}/{max_retries})"
                    )
                    time.sleep(delay)
                    delay *= 2
        return wrapper
    return decorator


def fetch_crypto_data(url: str, params: dict = None) -> dict:
    """Fetch cryptocurrency data from an API endpoint with retry handling."""
    @retry_network_op(max_retries=4, backoff_factor=1.5)
    def _execute_request():
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    return _execute_request()