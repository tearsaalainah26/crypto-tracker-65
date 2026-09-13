from typing import Dict, List, Optional, Union

def format_price(amount: float, symbol: str = 'USD') -> str:
    """
    Format crypto price as a currency string.

    :param amount: The numeric value of the asset.
    :param symbol: Currency code (default USD).
    :return: String representation with currency symbol.
    """
    return f"{symbol} {amount:,.2f}"

def calculate_portfolio_value(holdings: List[Dict[str, float]]) -> float:
    """
    Calculate total value of a list of assets.

    :param holdings: List of dicts containing 'quantity' and 'price'.
    :return: Total portfolio valuation as float.
    """
    return sum(item.get('quantity', 0.0) * item.get('price', 0.0) for item in holdings)

def get_asset_change_percentage(current: float, previous: float) -> Optional[float]:
    """
    Calculate percentage change between two price points.

    :param current: Current market price.
    :param previous: Historical price for comparison.
    :return: Percentage change or None if previous is zero.
    """
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100

def validate_ticker(ticker: str) -> bool:
    """
    Check if the ticker string matches standard crypto naming.

    :param ticker: The crypto symbol string.
    :return: Boolean indicating valid formatting.
    """
    return isinstance(ticker, str) and ticker.isalnum() and len(ticker) <= 10