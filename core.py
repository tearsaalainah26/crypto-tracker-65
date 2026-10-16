import requests
from typing import Dict, Optional

class CryptoTracker:
    """Core engine for crypto price tracking."""

    def __init__(self, base_url: str = "https://api.coingecko.com/api/v3"):
        self.base_url = base_url
        self.session = requests.Session()

    def fetch_price(self, coin_id: str, currency: str = "usd") -> Optional[float]:
        """Retrieve current price for a given coin identifier."""
        endpoint = f"{self.base_url}/simple/price"
        params = {"ids": coin_id, "vs_currencies": currency}
        
        try:
            response = self.session.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get(coin_id, {}).get(currency)
        except (requests.RequestException, ValueError):
            return None

    def get_market_data(self, coin_ids: list) -> Dict[str, float]:
        """Batch processing for multiple coin price updates."""
        results = {}
        for coin in coin_ids:
            price = self.fetch_price(coin)
            if price:
                results[coin] = price
        return results

if __name__ == "__main__":
    tracker = CryptoTracker()
    print(tracker.get_market_data(["bitcoin", "ethereum"]))
