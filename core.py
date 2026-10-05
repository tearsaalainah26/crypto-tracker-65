import functools
from typing import Dict, Any
from collections import deque

# Cache depth for frequent ticker updates
CACHE_SIZE = 128

class DataProcessor:
    """Core processing engine with memoization for high-frequency data."""
    
    def __init__(self):
        self._history = deque(maxlen=CACHE_SIZE)

    @functools.lru_cache(maxsize=CACHE_SIZE)
    def normalize_price(self, pair: str, price: float) -> float:
        """Standardize float precision for crypto market pairs."""
        return round(float(price), 8)

    def batch_process_rates(self, data: Dict[str, float]) -> Dict[str, float]:
        """Optimization via cached normalization calls."""
        return {
            pair: self.normalize_price(pair, rate)
            for pair, rate in data.items()
        }

    def get_latest_snapshot(self) -> list:
        """Retrieve processed data cache state."""
        return list(self._history)

# Singleton instance for core engine
engine = DataProcessor()