import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_on_failure(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to implement exponential backoff for network requests."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error(f"Function {func.__name__} failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator