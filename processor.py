import time
import requests
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

class NetworkProcessor:
    """Handles resilient network operations for crypto-tracker-65."""

    def __init__(self, max_retries: int = 3, delay: float = 2.0):
        self.max_retries = max_retries
        self.delay = delay

    def execute_with_retry(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        """Executes a network function with exponential backoff."""
        last_exception = None
        
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except (requests.exceptions.RequestException, ConnectionError) as e:
                last_exception = e
                wait_time = self.delay * (2 ** attempt)
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
        
        logger.error("Max retries reached for network operation.")
        raise last_exception

def fetch_market_data(url: str):
    """Example request handler for crypto data."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()