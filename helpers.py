"""Helper functions for formatting and calculations in crypto-tracker-65."""

from typing import Dict, Union


def format_currency(amount: Union[float, int], currency_symbol: str = "$") -> str:
    """Format a numeric crypto amount into a readable currency string.
    
    Args:
        amount: The monetary value to format.
        currency_symbol: The symbol to prepend.
        
    Returns:
        Formatted string with two decimal places and commas.
    """
    return f"{currency_symbol}{amount:,.2f}"


def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculate the percentage change between two prices.
    
    Args:
        old_price: The baseline price.
        new_price: The current price.
        
    Returns:
        Percentage difference as a float.
    """
    if old_price == 0.0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100.0


def parse_ticker_data(raw_data: Dict[str, Union[str, float]]) -> Dict[str, Union[str, float]]:
    """Sanitize and structure raw ticker data from exchanges.
    
    Args:
        raw_data: Dictionary containing raw API response fields.
        
    Returns:
        Cleaned dictionary with standardized keys and types.
    """
    cleaned: Dict[str, Union[str, float]] = {
        "symbol": str(raw_data.get("symbol", "UNKNOWN")).upper(),
        "price": float(raw_data.get("price", 0.0)),
        "volume": float(raw_data.get("volume", 0.0))
    }
    return cleaned
