from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

def format_crypto_price(price: float, symbol: str = "USD") -> str:
    """
    Format raw float price into a standardized string representation.

    Args:
        price: The numeric price value of the asset.
        symbol: Currency identifier, defaults to USD.

    Returns:
        Formatted string with currency symbol and precision.
    """
    if price <= 0:
        return f"N/A {symbol}"
    return f"{price:,.2f} {symbol}"

def parse_api_response(data: Dict[str, Any], key: str) -> Optional[float]:
    """
    Extract and validate numeric data from nested dictionary structures.

    Args:
        data: API response payload.
        key: Target key to extract from payload.

    Returns:
        The extracted float value or None if key is missing or invalid.
    """
    try:
        value = data.get(key)
        if value is None:
            return None
        return float(value)
    except (ValueError, TypeError) as e:
        logger.error("failed to parse api field %s: %s", key, e)
        return None

def calculate_percentage_change(current: float, previous: float) -> float:
    """
    Calculate the percentage difference between two price points.

    Args:
        current: Current market price.
        previous: Historical market price.

    Returns:
        Percentage change as a float.
    """
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100