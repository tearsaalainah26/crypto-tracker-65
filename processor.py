from typing import Dict, List, Optional
from decimal import Decimal

def calculate_portfolio_value(holdings: Dict[str, Decimal], market_data: Dict[str, Decimal]) -> Decimal:
    """Calculates total value of crypto assets in USD."""
    total_value = Decimal('0.00')
    for asset, amount in holdings.items():
        price = market_data.get(asset, Decimal('0.00'))
        total_value += amount * price
    return total_value.quantize(Decimal('0.01'))

def sanitize_market_data(raw_data: List[Dict]) -> Dict[str, Decimal]:
    """Converts raw API list into normalized symbol-to-price mapping."""
    processed = {}
    for entry in raw_data:
        symbol = entry.get('symbol', '').upper()
        price = entry.get('price', '0')
        try:
            processed[symbol] = Decimal(str(price))
        except (ValueError, TypeError):
            continue
    return processed

def get_asset_delta(current_price: Decimal, previous_price: Decimal) -> float:
    """Calculates percentage change between price points."""
    if previous_price == 0:
        return 0.0
    delta = ((current_price - previous_price) / previous_price) * 100
    return float(round(delta, 2))