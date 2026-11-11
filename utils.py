from typing import Dict, Union, Optional
import logging

# Configure logging for crypto-tracker-65
logger = logging.getLogger(__name__)

def format_price(price: float, symbol: str = "USD") -> str:
    """Formats a float price into a human-readable currency string."""
    return f"{price:,.2f} {symbol}"

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculates percentage change between two price points."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def validate_ticker(ticker: str) -> bool:
    """Checks if the provided crypto ticker is alphanumeric and valid length."""
    return ticker.isalnum() and 2 <= len(ticker) <= 10

def parse_api_response(data: Dict[str, Union[str, float]]) -> Optional[Dict[str, float]]:
    """Extracts core price data from raw API dictionary response."""
    try:
        return {
            "price": float(data.get("price", 0.0)),
            "volume": float(data.get("volume", 0.0))
        }
    except (ValueError, TypeError) as e:
        logger.error(f"failed to parse response: {e}")
        return None