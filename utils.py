import logging
import time
from functools import wraps
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Decorator that retries network calls with exponential backoff for crypto APIs."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            "Network operation '%s' failed after %d attempts: %s",
                            func.__name__, max_retries, err
                        )
                        raise err
                    
                    logger.warning(
                        "Attempt %d/%d for '%s' failed (%s). Retrying in %.1fs...",
                        attempt, max_retries, func.__name__, err, delay
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator
