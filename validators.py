import time
import functools
import logging

# crypto-tracker-65 network retry handler
logger = logging.getLogger(__name__)

def retry_network_call(max_retries=3, delay=2.0, backoff=2):
    """Decorator to retry network-dependent functions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"Max retries reached for {func.__name__}")
                        raise e
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def validate_ticker(ticker: str) -> bool:
    """Ensures ticker format matches crypto exchange standards."""
    if not ticker or not isinstance(ticker, str):
        return False
    return ticker.isalnum() and len(ticker) <= 10