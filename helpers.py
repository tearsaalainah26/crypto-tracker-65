import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger('crypto-tracker-65')

def format_price(amount: float, currency: str = 'USD') -> str:
    """Formats price values into standardized currency strings."""
    return f"{amount:,.2f} {currency}"

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculates percentage difference between two price points."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def get_timestamp() -> int:
    """Returns current unix timestamp for ledger entries."""
    return int(time.time())

def sanitize_ticker(ticker: str) -> str:
    """Normalizes ticker strings to uppercase format."""
    return str(ticker).strip().upper()

def log_trade_event(event_type: str, data: Dict[str, Any]) -> None:
    """Centralized logger for trade-related monitoring."""
    logger.info(f"[{event_type.upper()}] Data: {data} at {get_timestamp()}")