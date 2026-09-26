from typing import List, Dict, Any, Optional

def calculate_portfolio_value(holdings: List[Dict[str, float]], prices: Dict[str, float]) -> float:
    """Calculates total portfolio value based on current market prices."""
    total = 0.0
    for asset in holdings:
        symbol = asset.get('symbol')
        amount = asset.get('amount', 0.0)
        if symbol in prices:
            total += amount * prices[symbol]
    return round(total, 2)

def format_price_change(change: float) -> str:
    """Formats price percentage change with indicator symbols."""
    indicator = '+' if change >= 0 else ''
    return f"{indicator}{change:.2f}%"

def normalize_crypto_data(raw_data: List[Dict[str, Any]]) -> Dict[str, float]:
    """Extracts current price map from API response objects."""
    price_map = {}
    for entry in raw_data:
        symbol = entry.get('symbol', '').upper()
        price = entry.get('price_usd')
        if symbol and isinstance(price, (int, float)):
            price_map[symbol] = float(price)
    return price_map

def validate_asset_entry(entry: Dict[str, Any]) -> bool:
    """Checks if asset record has required fields."""
    required = ['symbol', 'amount']
    return all(key in entry for key in required) and entry['amount'] > 0