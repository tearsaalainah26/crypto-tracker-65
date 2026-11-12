import functools
import time
from typing import Dict, Any

# Cache for price data to reduce redundant API calls
# TTL set to 30 seconds for real-time crypto price updates
CACHE_TTL = 30
_price_cache: Dict[str, tuple[float, float]] = {}

@functools.lru_cache(maxsize=128)
def get_normalized_ticker(ticker: str) -> str:
    return ticker.strip().upper()

def get_cached_price(symbol: str, fetch_func: callable) -> float:
    """Fetches price using cache lookup with TTL expiry."""
    ticker = get_normalized_ticker(symbol)
    now = time.time()

    if ticker in _price_cache:
        price, timestamp = _price_cache[ticker]
        if now - timestamp < CACHE_TTL:
            return price

    # Cache miss or expired
    new_price = fetch_func(ticker)
    _price_cache[ticker] = (new_price, now)
    return new_price

def batch_process_prices(tickers: list, fetch_func: callable) -> Dict[str, float]:
    """Optimized batch retrieval using dictionary comprehension."""
    return {ticker: get_cached_price(ticker, fetch_func) for ticker in tickers}

def clear_stale_cache(threshold: int = 300) -> None:
    """Manual cleanup of the memory cache."""
    now = time.time()
    keys_to_delete = [
        ticker for ticker, (_, ts) in _price_cache.items()
        if now - ts > threshold
    ]
    for key in keys_to_delete:
        del _price_cache[key]