import time
import requests
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(func: Callable, retries: int = 3, delay: int = 2) -> Any:
    """Executes network operations with exponential backoff."""
    for attempt in range(retries):
        try:
            return func()
        except (requests.RequestException, ConnectionError) as e:
            if attempt == retries - 1:
                logger.error(f"Final attempt failed: {e}")
                raise
            logger.warning(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
            time.sleep(delay)
            delay *= 2

class CryptoDataProcessor:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_price(self, symbol: str) -> dict:
        """Fetches price data for a given crypto symbol."""
        def _request():
            response = requests.get(f"{self.api_url}/price/{symbol}", timeout=10)
            response.raise_for_status()
            return response.json()

        return with_retry(_request)

if __name__ == "__main__":
    processor = CryptoDataProcessor("https://api.crypto-tracker-65.io")
    try:
        data = processor.fetch_price("BTC")
        print(data)
    except Exception as err:
        print(f"Critical failure: {err}")