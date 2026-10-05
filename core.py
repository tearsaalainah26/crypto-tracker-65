from typing import Dict, List, Optional

def format_price(price: float, symbol: str) -> str:
    """Formats crypto price with currency symbol and precision."""
    if price < 1.0:
        return f"{symbol}{price:.6f}"
    return f"{symbol}{price:,.2f}"

def calculate_portfolio_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Calculates total value of portfolio based on current market prices."""
    total = 0.0
    for asset, amount in holdings.items():
        price = prices.get(asset, 0.0)
        total += amount * price
    return total

def filter_by_threshold(assets: List[Dict], threshold: float) -> List[Dict]:
    """Filters assets that meet a minimum value requirement."""
    return [item for item in assets if item.get('price', 0) >= threshold]

def normalize_asset_name(name: str) -> str:
    """Converts asset symbols to uppercase for standardized lookups."""
    return name.strip().upper()