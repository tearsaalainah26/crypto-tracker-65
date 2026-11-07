import time
from typing import Dict, List, Optional
from functools import lru_cache
from dataclasses import dataclass


@dataclass
class TickerData:
    symbol: str
    price: float
    volume: float
    timestamp: float


class CryptoEngine:
    """Core processing engine for real-time crypto market metrics."""

    def __init__(self, max_history: int = 1000):
        self.max_history = max_history
        self._price_history: Dict[str, List[float]] = {}
        self._volume_history: Dict[str, List[float]] = {}

    def ingest_ticker(self, ticker: TickerData) -> None:
        """Ingest new ticker update and clear relevant cache entries."""
        symbol = ticker.symbol.upper()
        if symbol not in self._price_history:
            self._price_history[symbol] = []
            self._volume_history[symbol] = []

        prices = self._price_history[symbol]
        volumes = self._volume_history[symbol]

        prices.append(ticker.price)
        volumes.append(ticker.volume)

        # Maintain sliding window history size limit
        if len(prices) > self.max_history:
            prices.pop(0)
            volumes.pop(0)

        # Invalidate cached calculation for updated symbol
        self.get_moving_average.cache_clear()

    @lru_cache(maxsize=128)
    def get_moving_average(self, symbol: str, window: int) -> Optional[float]:
        """Calculates simple moving average using cached lookup."""
        prices = self._price_history.get(symbol.upper(), [])
        if not prices or len(prices) < window:
            return None

        # Slice latest window values and compute mean
        sub_series = prices[-window:]
        return sum(sub_series) / window

    def calculate_batch_volatility(self, symbols: List[str], window: int) -> Dict[str, float]:
        """Compute relative standard deviation across multiple assets in a single pass."""
        results = {}
        for symbol in symbols:
            sym_upper = symbol.upper()
            prices = self._price_history.get(sym_upper, [])
            if len(prices) < window:
                continue

            slice_prices = prices[-window:]
            mean = sum(slice_prices) / window
            variance = sum((x - mean) ** 2 for x in slice_prices) / window
            std_dev = variance ** 0.5

            results[sym_upper] = round(std_dev / mean, 6) if mean != 0 else 0.0

        return results
