import functools
import time
import logging
from typing import Callable, Any

# Configure logger for core module performance tracking
logger = logging.getLogger('crypto-tracker-65.processor')

@functools.lru_cache(maxsize=128)
def get_normalized_price(symbol: str, price: float) -> float:
    """Cache normalized price calculations to reduce CPU cycles."""
    return round(float(price), 8)

def performance_monitor(func: Callable) -> Callable:
    """Decorator for tracking execution time of critical modules."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        if duration > 0.1:
            logger.debug(f'Slow execution in {func.__name__}: {duration:.4f}s')
        return result
    return wrapper

@performance_monitor
def process_batch(data: list[dict]) -> list[float]:
    """Efficient batch processing of incoming price tickers."""
    processed = []
    for entry in data:
        # Directly map using cached utility
        val = get_normalized_price(entry.get('s', ''), entry.get('p', 0.0))
        processed.append(val)
    return processed