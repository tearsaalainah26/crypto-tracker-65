import logging
from typing import Dict, Any, Optional

# Set up local module logger
logger = logging.getLogger('crypto-tracker-65')

def format_price(amount: float, symbol: str = 'USD') -> str:
    """Formats crypto price with currency suffix."""
    return f"{amount:,.2f} {symbol}"

def sanitize_ticker(ticker: str) -> str:
    """Normalizes ticker symbols for API requests."""
    return ticker.strip().upper()

def get_percentage_change(current: float, previous: float) -> Optional[float]:
    """Calculates percentage difference between two values."""
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100

def validate_response(data: Dict[str, Any]) -> bool:
    """Verifies API response integrity."""
    required_keys = {'price', 'symbol', 'timestamp'}
    return all(key in data for key in required_keys)

def log_performance(ticker: str, duration: float) -> None:
    """Logs processing latency for telemetry."""
    logger.info(f"Processed {ticker} in {duration:.4f}s")