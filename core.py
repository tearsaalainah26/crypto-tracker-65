import asyncio
from collections import deque
from typing import Dict, List, Optional, Tuple


class PriceTrackerCore:
    """High-performance crypto price aggregation and metric calculation core."""

    def __init__(self, window_size: int = 100):
        self.window_size = window_size
        self._price_buffers: Dict[str, deque] = {}
        self._cache: Dict[str, Tuple[float, float, float]] = {}

    def update_price(self, symbol: str, price: float) -> None:
        """In-place update of price window with dynamic cache invalidation."""
        if symbol not in self._price_buffers:
            self._price_buffers[symbol] = deque(maxlen=self.window_size)

        self._price_buffers[symbol].append(price)
        self._cache.pop(symbol, None)

    def get_metrics(self, symbol: str) -> Optional[Dict[str, float]]:
        """Returns cached or freshly computed min, max, and moving average."""
        buffer = self._price_buffers.get(symbol)
        if not buffer:
            return None

        if symbol in self._cache:
            min_p, max_p, avg_p = self._cache[symbol]
        else:
            min_p = min(buffer)
            max_p = max(buffer)
            avg_p = sum(buffer) / len(buffer)
            self._cache[symbol] = (min_p, max_p, avg_p)

        return {
            "min": round(min_p, 4),
            "max": round(max_p, 4),
            "avg": round(avg_p, 4),
            "samples": len(buffer),
        }

    def batch_process_ticks(self, ticks: List[Tuple[str, float]]) -> Dict[str, Dict[str, float]]:
        """Process multiple price ticks efficiently in a single batch."""
        updated_symbols = set()
        for symbol, price in ticks:
            if symbol not in self._price_buffers:
                self._price_buffers[symbol] = deque(maxlen=self.window_size)
            self._price_buffers[symbol].append(price)
            updated_symbols.add(symbol)

        for sym in updated_symbols:
            self._cache.pop(sym, None)

        results = {}
        for sym in updated_symbols:
            metrics = self.get_metrics(sym)
            if metrics:
                results[sym] = metrics

        return results