import time
from typing import Dict, Optional, Tuple

class PriceCache:
    """An in-memory TTL cache to store token prices and avoid redundant lookups."""
    def __init__(self, ttl_seconds: int = 10):
        self.ttl: int = ttl_seconds
        self._cache: Dict[str, Tuple[float, float]] = {}

    def get(self, symbol: str) -> Optional[float]:
        """Retrieve token price if it exists and has not expired."""
        if symbol not in self._cache:
            return None
        price, timestamp = self._cache[symbol]
        if time.time() - timestamp > self.ttl:
            del self._cache[symbol]
            return None
        return price

    def set(self, symbol: str, price: float) -> None:
        """Cache token price with current epoch timestamp."""
        self._cache[symbol] = (price, time.time())

class CorePriceTracker:
    """Optimized price retrieval tracking subsystem."""
    def __init__(self, cache_ttl: int = 5):
        self.cache = PriceCache(ttl_seconds=cache_ttl)

    def fetch_mock_price(self, symbol: str) -> float:
        """Simulate api call with noticeable delay for performance testing."""
        time.sleep(0.2)
        mock_prices = {"BTC": 65000.0, "ETH": 3500.0, "SOL": 140.0}
        return mock_prices.get(symbol.upper(), 0.0)

    def get_price(self, symbol: str) -> float:
        """Fetch token price utilizing optimized ttl cache to reduce api overhead."""
        symbol_upper = symbol.upper()
        cached_price = self.cache.get(symbol_upper)
        if cached_price is not None:
            return cached_price
        
        fresh_price = self.fetch_mock_price(symbol_upper)
        self.cache.set(symbol_upper, fresh_price)
        return fresh_price