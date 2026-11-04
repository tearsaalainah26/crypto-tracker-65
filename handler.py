import time
import json
import logging
import urllib.request
import urllib.error
from functools import wraps
from typing import Callable, Any, Dict, Optional, Tuple

logger = logging.getLogger(__name__)

def retry_on_failure(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[type, ...] = (urllib.error.URLError, TimeoutError, OSError)
) -> Callable:
    """Decorator that retries a network operation with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(f"Final attempt {attempt}/{max_retries} failed for {func.__name__}: {err}")
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for {func.__name__}: {err}. "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator


class CryptoApiHandler:
    """Handles public API requests for market data with built-in retry logic."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    @retry_on_failure(max_retries=3, delay=0.5, backoff=2.0)
    def fetch_ticker(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Fetch current spot ticker price for a cryptocurrency pair."""
        endpoint = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
        request = urllib.request.Request(endpoint, headers={"User-Agent": "crypto-tracker/1.0"})

        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            if response.status == 200:
                payload = json.loads(response.read().decode("utf-8"))
                return {
                    "symbol": payload.get("symbol"),
                    "price": float(payload.get("price", 0.0))
                }
        return None
