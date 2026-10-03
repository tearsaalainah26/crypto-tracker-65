import functools
import time
from typing import Callable, Any, Dict

# Cache for crypto price calculations to reduce API load
_price_cache: Dict[str, tuple[float, float]] = {}
CACHE_EXPIRY = 60  # seconds

def memoize_price_calculation(func: Callable) -> Callable:
    """Decorator to cache result of expensive crypto math."""
    @functools.wraps(func)
    def wrapper(symbol: str, *args, **kwargs) -> Any:
        current_time = time.time()
        if symbol in _price_cache:
            val, timestamp = _price_cache[symbol]
            if current_time - timestamp < CACHE_EXPIRY:
                return val
        
        result = func(symbol, *args, **kwargs)
        _price_cache[symbol] = (result, current_time)
        return result
    return wrapper

@memoize_price_calculation
def calculate_volatility(symbol: str, price_history: list[float]) -> float:
    """Calculates simple variance for price history."""
    if not price_history:
        return 0.0
    mean = sum(price_history) / len(price_history)
    variance = sum((x - mean) ** 2 for x in price_history) / len(price_history)
    return float(variance ** 0.5)

def clear_stale_cache() -> None:
    """Cleanup function to free memory."""
    global _price_cache
    _price_cache = {k: v for k, v in _price_cache.items() 
                    if time.time() - v[1] < CACHE_EXPIRY}