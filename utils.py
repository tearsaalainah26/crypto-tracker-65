import time
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def format_currency(value: float, symbol: str = "USD") -> str:
    """Formats float values into human-readable currency strings."""
    return f"{value:,.2f} {symbol}"

def rate_limited_request(func, *args, **kwargs):
    """Retry wrapper with backoff for network instability."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == max_retries - 1:
                logger.error(f"Final attempt failed: {e}")
                raise
            time.sleep(2 ** attempt)

def sanitize_ticker(ticker: str) -> str:
    """Ensures crypto ticker formatting."""
    return ticker.strip().upper().replace("/", "-")

def calculate_delta(current: float, previous: float) -> float:
    """Computes percentage change between two values."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100