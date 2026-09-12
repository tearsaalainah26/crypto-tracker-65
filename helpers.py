import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def format_price(amount: float, currency: str = "USD") -> str:
    """Formats crypto price for standardized display."""
    return f"{amount:,.2f} {currency}"

def sanitize_ticker(ticker: str) -> str:
    """Ensures ticker format consistency."""
    return ticker.strip().upper()

def retry_request(func, retries: int = 3, delay: int = 2):
    """Decorator logic for unstable network requests."""
    def wrapper(*args, **kwargs):
        last_error = None
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_error = e
                time.sleep(delay)
        logger.error(f"Failed after {retries} attempts: {last_error}")
        return None
    return wrapper

def parse_crypto_data(data: Dict[str, Any]) -> Optional[Dict[str, float]]:
    """Extracts essential market fields from API response."""
    try:
        return {
            "price": float(data.get("price", 0)),
            "volume": float(data.get("volume_24h", 0)),
            "timestamp": time.time()
        }
    except (ValueError, TypeError):
        return None