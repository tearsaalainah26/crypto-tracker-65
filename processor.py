from typing import List, Dict, Optional

def calculate_portfolio_value(holdings: List[Dict], prices: Dict[str, float]) -> float:
    """Calculates total value of crypto holdings based on market prices."""
    total_value = 0.0
    for holding in holdings:
        symbol = holding.get("symbol")
        amount = holding.get("amount", 0.0)
        if symbol in prices:
            total_value += amount * prices[symbol]
    return round(total_value, 2)

def format_price_change(change_percent: float) -> str:
    """Formats price percentage change for display."""
    sign = "+" if change_percent > 0 else ""
    return f"{sign}{change_percent:.2f}%"

def filter_by_threshold(market_data: List[Dict], threshold: float) -> List[Dict]:
    """Filters crypto assets exceeding a specific volume threshold."""
    return [item for item in market_data if item.get("volume", 0) >= threshold]

def normalize_symbol(symbol: str) -> str:
    """Standardizes ticker symbols to uppercase."""
    return symbol.strip().upper()

def get_asset_info(data: Dict, symbol: str) -> Optional[Dict]:
    """Retrieves specific asset metadata from response object."""
    normalized = normalize_symbol(symbol)
    return data.get(normalized, None)