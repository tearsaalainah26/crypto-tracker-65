import functools
import time
from typing import Callable, Any

def memoize_data(ttl: int = 60):
    """Cache function results to optimize API calls."""
    cache = {}

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process_prices(prices: list[float], factor: float = 1.0) -> list[float]:
    """Vectorized-style list comprehension for price normalization."""
    return [p * factor for p in prices]

def get_weighted_average(data: dict[str, float]) -> float:
    """Efficient computation of weighted asset values."""
    if not data:
        return 0.0
    total_value = sum(data.values())
    return total_value / len(data) if len(data) > 0 else 0.0