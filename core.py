import time
from functools import lru_cache
from typing import Dict, List

class PerformanceOptimizer:
    """Core performance optimization engine for crypto price tracking."""
    
    def __init__(self, cache_ttl: int = 5) -> None:
        self.cache_ttl = cache_ttl
        self._last_flush = time.time()

    @lru_cache(maxsize=1024)
    def calculate_moving_average(self, symbol: str, prices_tuple: tuple) -> float:
        """Calculate cached moving average for price tuples."""
        if not prices_tuple:
            return 0.0
        return sum(prices_tuple) / len(prices_tuple)

    def batch_process_ticks(self, raw_ticks: List[Dict[str, float]]) -> Dict[str, float]:
        """Process bulk crypto ticks with memory footprint optimization."""
        processed_data: Dict[str, float] = {}
        
        for tick in raw_ticks:
            symbol = tick.get("symbol")
            price = tick.get("price")
            if symbol and price:
                processed_data[symbol] = float(price)
                
        current_time = time.time()
        if current_time - self._last_flush > 60:
            self.calculate_moving_average.cache_clear()
            self._last_flush = current_time
            
        return processed_data
