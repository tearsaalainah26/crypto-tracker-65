import time
import logging
import functools
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_on_failure(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_retries = 0
            current_delay = delay
            
            while current_retries < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, Exception) as e:
                    current_retries += 1
                    if current_retries >= retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Retry {current_retries}/{retries} for {func.__name__} after error: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator