import time
from functools import lru_cache
from typing import Dict, List

@lru_cache(maxsize=128)
def calculate_moving_average(prices: tuple, window: int) -> float:
    """Calculate the simple moving average for cached crypto prices."""
    if len(prices) < window:
        return sum(prices) / len(prices) if prices else 0.0
    return sum(prices[-window:]) / window

class PerformanceOptimizer:
    """Optimized batch processor for crypto ticker data."""
    
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size
        self._cache: Dict[str, List[float]] = {}

    def process_ticks(self, symbol: str, price: float) -> float:
        """Process incoming ticks and return the optimized moving average."""
        if symbol not in self._cache:
            self._cache[symbol] = []
            
        history = self._cache[symbol]
        history.append(price)
        
        # Keep memory footprint bounded
        if len(history) > self.batch_size:
            self._cache[symbol] = history[-self.batch_size:]
            
        # Convert to tuple for hashable caching
        return calculate_moving_average(tuple(self._cache[symbol]), window=20)