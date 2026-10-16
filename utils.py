import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_request(max_retries: int = 3, backoff: float = 2.0):
    """Decorator for retrying network requests on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            delay = backoff
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(f"Max retries reached for {func.__name__}: {e}")
                        raise
                    logger.warning(f"Retry {retries}/{max_retries} for {func.__name__} after {delay}s error: {e}")
                    time.sleep(delay)
                    delay *= 2
        return wrapper
    return decorator