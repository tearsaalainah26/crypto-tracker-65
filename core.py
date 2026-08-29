import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
import requests

class CryptoCore:
    """Core module for tracking cryptocurrency prices with performance optimizations."""

    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers
        self.price_cache = {}
        self.last_fetch = {}

    @lru_cache(maxsize=128)
    def _fetch_single_price(self, coin_id: str) -> float:
        """Fetch price for a single coin. Uses LRU cache for repeated calls."""
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return float(data.get(coin_id, {}).get('usd', 0.0))
            return 0.0
        except Exception:
            return 0.0

    def fetch_prices(self, coin_ids: list) -> dict:
        """Fetch prices concurrently using thread pool for better performance."""
        prices = {}
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_coin = {executor.submit(self._fetch_single_price, coin): coin for coin in coin_ids}
            for future in as_completed(future_to_coin):
                coin = future_to_coin[future]
                try:
                    prices[coin] = future.result()
                except Exception:
                    prices[coin] = 0.0
        return prices

    def get_tracked_prices(self, coins: list) -> dict:
        """Get prices, applying cache where possible to optimize."""
        current_time = time.time()
        to_fetch = []
        results = {}
        for coin in coins:
            if coin in self.price_cache and current_time - self.last_fetch.get(coin, 0) < 60:
                results[coin] = self.price_cache[coin]
            else:
                to_fetch.append(coin)
        if to_fetch:
            new_prices = self.fetch_prices(to_fetch)
            for coin, price in new_prices.items():
                self.price_cache[coin] = price
                self.last_fetch[coin] = current_time
            results.update(new_prices)
        return results
