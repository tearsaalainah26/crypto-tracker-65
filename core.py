import json
import logging
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, Tuple, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def retry_network_call(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: Tuple[type, ...] = (urllib.error.URLError, TimeoutError, OSError),
) -> Callable[[F], F]:
    """Decorator that retries network operations with exponential backoff."""
    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            delay = 1.0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempt += 1
                    if attempt >= max_retries:
                        logger.error("Operation %s failed after %d attempts: %s", func.__name__, max_retries, err)
                        raise
                    
                    logger.warning(
                        "Network attempt %d/%d failed for %s: %s. Retrying in %.1fs...",
                        attempt,
                        max_retries,
                        func.__name__,
                        err,
                        delay,
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper  # type: ignore
    return decorator


class CryptoTrackerCore:
    """Core client for handling crypto asset price requests."""

    def __init__(self, base_url: str = "https://api.coingecko.com/api/v3") -> None:
        self.base_url = base_url.rstrip("/")

    @retry_network_call(max_retries=3, backoff_factor=2.0)
    def get_spot_price(self, coin_id: str, currency: str = "usd") -> Dict[str, Any]:
        """Fetch current spot price for a cryptocurrency asset."""
        endpoint = f"{self.base_url}/simple/price?ids={coin_id}&vs_currencies={currency}"
        request = urllib.request.Request(
            endpoint,
            headers={"User-Agent": "CryptoTracker/1.0"}
        )
        
        with urllib.request.urlopen(request, timeout=5) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
