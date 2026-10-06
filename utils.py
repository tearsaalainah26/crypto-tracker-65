import functools
import time
from typing import Any, Callable, Dict

# Cache for crypto price calculations
_price_cache: Dict[str, Any] = {}
_cache_expiry: Dict[str, float] = {}
CACHE_TTL = 30  # seconds

def memoize_crypto_data(func: Callable) -> Callable:
    """Decorator for caching ticker calculations to reduce CPU load."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = str(args) + str(kwargs)
        now = time.time()

        if key in _price_cache and (now - _cache_expiry.get(key, 0)) < CACHE_TTL:
            return _price_cache[key]

        result = func(*args, **kwargs)
        _price_cache[key] = result
        _cache_expiry[key] = now
        return result

    return wrapper

def batch_process_prices(price_list: list) -> list:
    """Vectorized-style approach for list transformation optimization."""
    # Minimize object creation overhead in processing loops
    return [p * 1.0001 for p in price_list if p > 0]

# Helper for clearing stale cache entries
def clear_stale_cache() -> None:
    """Cleanup of expired cache entries."""
    now = time.time()
    expired = [k for k, t in _cache_expiry.items() if (now - t) > CACHE_TTL]
    for key in expired:
        _price_cache.pop(key, None)
        _cache_expiry.pop(key, None)