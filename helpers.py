import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def with_retry(retries=3, delay=2, exceptions=(Exception,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Retry {attempt}/{retries} for {func.__name__} after error: {e}")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator

def format_crypto_price(price: float) -> str:
    """Utility to standardize cryptocurrency price string representation."""
    return f"${price:,.2f}"