from collections import deque
from dataclasses import dataclass
from typing import Dict, List


@dataclass(slots=True)
class TradeTick:
    symbol: str
    price: float
    volume: float
    timestamp: float


class BatchStreamProcessor:
    """High-performance stream processor for cryptocurrency trade ticks."""

    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self._buffers: Dict[str, deque] = {}
        self._totals: Dict[str, Dict[str, float]] = {}

    def process_tick(self, tick: TradeTick) -> Dict[str, float]:
        """Process a single trade tick with O(1) rolling metrics update."""
        symbol = tick.symbol
        if symbol not in self._buffers:
            self._buffers[symbol] = deque()
            self._totals[symbol] = {"volume_price": 0.0, "total_volume": 0.0}

        buffer = self._buffers[symbol]
        totals = self._totals[symbol]

        vol_price = tick.price * tick.volume
        buffer.append((tick.price, tick.volume, vol_price))
        totals["volume_price"] += vol_price
        totals["total_volume"] += tick.volume

        while len(buffer) > self.window_size:
            _, old_vol, old_vol_price = buffer.popleft()
            totals["volume_price"] -= old_vol_price
            totals["total_volume"] -= old_vol

        vwap = totals["volume_price"] / totals["total_volume"] if totals["total_volume"] > 0 else 0.0

        return {
            "symbol": symbol,
            "vwap": round(vwap, 8),
            "latest_price": tick.price,
            "buffer_size": len(buffer)
        }

    def batch_process(self, ticks: List[TradeTick]) -> List[Dict[str, float]]:
        """Process a batch of incoming ticks in memory."""
        return [self.process_tick(tick) for tick in ticks]
