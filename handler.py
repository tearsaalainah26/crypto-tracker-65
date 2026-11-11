from typing import Dict, List, Optional
import requests

class CryptoDataHandler:
    """Handles retrieval and formatting of cryptocurrency market data."""

    def __init__(self, base_url: str = "https://api.coingecko.com/api/v3") -> None:
        self.base_url: str = base_url

    def fetch_price(self, coin_id: str, currency: str = "usd") -> Optional[float]:
        """Fetches the current price of a specific coin by ID."""
        url: str = f"{self.base_url}/simple/price"
        params: Dict[str, str] = {"ids": coin_id, "vs_currencies": currency}
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data: Dict = response.json()
            return float(data.get(coin_id, {}).get(currency, 0.0))
        except (requests.RequestException, ValueError, KeyError):
            return None

    def get_supported_coins(self) -> List[str]:
        """Returns a list of coin IDs supported by the API."""
        url: str = f"{self.base_url}/coins/list"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data: List[Dict[str, str]] = response.json()
            return [coin["id"] for coin in data if "id" in coin]
        except requests.RequestException:
            return []