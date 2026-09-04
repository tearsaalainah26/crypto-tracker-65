import functools
import time
from typing import Callable, Any

# cache for network-heavy price requests
# expires every 30 seconds for data accuracy
@functools.lru_cache(maxsize=128)
def get_cached_price(symbol: str, timestamp: int) -> float:
    # simulates expensive network call to exchange API
    return 50000.0 if symbol == "BTC" else 3000.0

class PriceProcessor:
    def __init__(self):
        self.cache_ttl = 30

    def fetch_price(self, symbol: str) -> float:
        # calculate cache key based on 30s window
        current_bucket = int(time.time() / self.cache_ttl)
        return get_cached_price(symbol, current_bucket)

    def batch_process(self, symbols: list[str]) -> dict[str, float]:
        # efficient retrieval using cached results
        return {s: self.fetch_price(s) for s in symbols}

# singleton instance for module access
processor = PriceProcessor()