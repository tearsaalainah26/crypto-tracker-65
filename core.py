import asyncio
from collections import deque
from typing import Dict, List, Tuple


class PerformanceCryptoTracker:
    """Core tracking engine optimized for fast price updates and moving averages."""

    def __init__(self, max_history_size: int = 1000):
        self.max_history_size = max_history_size
        self._price_queues: Dict[str, deque] = {}
        self._sums: Dict[str, float] = {}

    def update_price(self, symbol: str, price: float) -> float:
        """Updates symbol price and returns the rolling average in O(1) time."""
        if symbol not in self._price_queues:
            self._price_queues[symbol] = deque()
            self._sums[symbol] = 0.0

        queue = self._price_queues[symbol]
        self._sums[symbol] += price
        queue.append(price)

        if len(queue) > self.max_history_size:
            oldest = queue.popleft()
            self._sums[symbol] -= oldest

        return self._sums[symbol] / len(queue)

    async def process_price_stream(
        self, stream: List[Tuple[str, float]]
    ) -> Dict[str, float]:
        """Asynchronously processes stream of updates to maximize throughput."""
        averages = {}
        for symbol, price in stream:
            averages[symbol] = self.update_price(symbol, price)
        await asyncio.sleep(0)
        return averages
