import functools
import time
from typing import Dict, Any

# global cache for ticker price lookups to minimize redundant network calls
_PRICE_CACHE: Dict[str, Dict[str, Any]] = {}
_CACHE_TTL = 30  # seconds

@functools.lru_cache(maxsize=128)
def get_normalized_ticker(symbol: str) -> str:
    """standardize crypto symbols for internal processing"""
    return symbol.strip().upper()

def get_cached_price(symbol: str, fetch_func: callable) -> float:
    """memoization pattern with expiration for crypto data"""
    now = time.time()
    ticker = get_normalized_ticker(symbol)

    if ticker in _PRICE_CACHE:
        data = _PRICE_CACHE[ticker]
        if now - data['timestamp'] < _CACHE_TTL:
            return data['price']

    # fetch fresh data if expired or missing
    price = fetch_func(ticker)
    _PRICE_CACHE[ticker] = {
        'price': price,
        'timestamp': now
    }
    return price

def batch_update_prices(symbols: list, fetch_func: callable) -> Dict[str, float]:
    """optimized bulk lookup for multiple trading pairs"""
    return {s: get_cached_price(s, fetch_func) for s in symbols}