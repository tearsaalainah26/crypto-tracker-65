from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

def format_currency(amount: float, symbol: str = 'USD') -> str:
    """Formats a numeric amount into a currency string."""
    return f"{amount:,.2f} {symbol}"

def calculate_percentage_change(current: float, previous: float) -> Optional[float]:
    """Calculates percentage change between two price points."""
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100

def filter_top_assets(assets: List[Dict[str, float]], threshold: float) -> List[Dict[str, float]]:
    """Filters assets with price higher than the provided threshold."""
    return [asset for asset in assets if asset.get("price", 0) >= threshold]

def normalize_ticker(ticker: str) -> str:
    """Converts ticker string to uppercase and strips whitespace."""
    return ticker.strip().upper()

def get_summary_report(data: List[Dict[str, float]]) -> Dict[str, float]:
    """Generates a simple average and total price summary."""
    if not data:
        return {"total": 0.0, "average": 0.0}
    
    prices = [item.get("price", 0) for item in data]
    total = sum(prices)
    return {
        "total": total,
        "average": total / len(prices)
    }