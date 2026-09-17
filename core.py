import requests
from typing import Dict, Optional

class CryptoTracker:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_price(self, symbol: str) -> Optional[float]:
        """Retrieves cryptocurrency price with error handling."""
        if not symbol or not isinstance(symbol, str):
            return None

        try:
            response = requests.get(f"{self.api_url}/price/{symbol}", timeout=5)
            response.raise_for_status()
            data = response.json()
            return float(data.get("price", 0.0))
        except requests.exceptions.RequestException as e:
            print(f"Network error for {symbol}: {e}")
            return None
        except (ValueError, TypeError, KeyError) as e:
            print(f"Data parsing error for {symbol}: {e}")
            return None

    def get_market_data(self, symbols: list) -> Dict[str, float]:
        """Batch processor for multiple currency symbols."""
        results = {}
        for symbol in symbols:
            price = self.fetch_price(symbol)
            if price is not None:
                results[symbol] = price
        return results