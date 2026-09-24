import functools
import time
from typing import Dict, Any

# Cache dictionary for crypto price lookups to reduce network overhead
_price_cache: Dict[str, Dict[str, Any]] = {}
CACHE_TTL = 60  # seconds

@functools.lru_cache(maxsize=128)
def get_normalized_ticker(ticker: str) -> str:
    return ticker.strip().upper()

def get_cached_price(symbol: str, fetch_func: callable) -> float:
    """Retrieves price with TTL-based memoization for crypto-tracker-65."""
    normalized = get_normalized_ticker(symbol)
    now = time.time()

    if normalized in _price_cache:
        data = _price_cache[normalized]
        if now - data['timestamp'] < CACHE_TTL:
            return data['price']

    # Fetch fresh price if cache miss or expired
    price = fetch_func(normalized)
    _price_cache[normalized] = {
        'price': price,
        'timestamp': now
    }
    return price

def clear_stale_cache(threshold: int = 300) -> None:
    """Maintenance function to prevent memory leaks in long-running processes."""
    now = time.time()
    keys_to_delete = [
        k for k, v in _price_cache.items() 
        if now - v['timestamp'] > threshold
    ]
    for k in keys_to_delete:
        del _price_cache[k]