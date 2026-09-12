import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('crypto-tracker-65')

def retry_network_call(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator to retry network operations on failure.
    Retries up to max_retries with an exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, Exception) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error(f"Final attempt failed after {max_retries} retries.")
            raise last_exception
        return wrapper
    return decorator