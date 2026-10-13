import time
from typing import Dict, List, Optional

class PriceAggregator:
    """Core engine for tracking and calculating cryptocurrency metrics with caching."""

    def __init__(self, cache_ttl_seconds: int = 5):
        self.cache_ttl = cache_ttl_seconds
        self._price_history: Dict[str, List[float]] = {}
        self._cache: Dict[str, tuple[float, float]] = {}

    def add_price(self, symbol: str, price: float) -> None:
        """Append a new price entry to the symbol history log."""
        symbol = symbol.upper()
        if symbol not in self._price_history:
            self._price_history[symbol] = []
        self._price_history[symbol].append(price)

    def get_moving_average(self, symbol: str, window: int = 10) -> Optional[float]:
        """Calculate moving average with time-based TTL cache optimization."""
        symbol = symbol.upper()
        history = self._price_history.get(symbol, [])
        if not history:
            return None

        cache_key = f"{symbol}_{window}_{len(history)}"
        now = time.time()

        if cache_key in self._cache:
            cached_time, cached_val = self._cache[cache_key]
            if now - cached_time < self.cache_ttl:
                return cached_val

        recent_prices = history[-window:]
        avg_price = sum(recent_prices) / len(recent_prices)
        self._cache[cache_key] = (now, avg_price)
        return round(avg_price, 4)

    def batch_calculate_volatility(self, symbols: List[str]) -> Dict[str, float]:
        """Compute variance metrics across multiple tokens in optimized batches."""
        results = {}
        for symbol in symbols:
            symbol = symbol.upper()
            prices = self._price_history.get(symbol, [])
            if len(prices) < 2:
                results[symbol] = 0.0
                continue

            mean = sum(prices) / len(prices)
            variance = sum((x - mean) ** 2 for x in prices) / len(prices)
            results[symbol] = round(variance ** 0.5, 4)

        return results