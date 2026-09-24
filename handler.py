import functools
import time
from typing import Dict, Any

# Cache for market data to reduce API calls
_price_cache: Dict[str, tuple[float, float]] = {}
CACHE_TTL = 30  # seconds

@functools.lru_cache(maxsize=128)
def get_normalized_ticker(symbol: str) -> str:
    return symbol.strip().upper()

def get_cached_price(symbol: str, fetch_func: callable) -> float:
    """Retrieves price with time-based invalidation."""
    normalized = get_normalized_ticker(symbol)
    now = time.time()

    if normalized in _price_cache:
        price, timestamp = _price_cache[normalized]
        if now - timestamp < CACHE_TTL:
            return price

    # Fetch fresh data if expired or missing
    new_price = fetch_func(normalized)
    _price_cache[normalized] = (new_price, now)
    return new_price

def batch_process_updates(updates: list[dict], fetch_func: callable) -> list[float]:
    """Optimized bulk processing using memoization."""
    results = []
    for update in updates:
        symbol = update.get('symbol', '')
        if symbol:
            price = get_cached_price(symbol, fetch_func)
            results.append(price)
    return results