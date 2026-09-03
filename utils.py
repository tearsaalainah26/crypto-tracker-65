from typing import Dict, Any, Optional

def format_crypto_price(price: float, currency: str = 'USD') -> str:
    """Formats a float price into a clean string representation."""
    if price <= 0:
        return f"0.00 {currency}"
    if price < 0.01:
        return f"{price:.8f} {currency}"
    return f"{price:,.2f} {currency}"

def validate_ticker_format(ticker: str) -> bool:
    """Checks if the ticker string matches expected crypto patterns."""
    return isinstance(ticker, str) and 2 <= len(ticker) <= 10 and ticker.isalnum()

def parse_api_response(data: Dict[str, Any], key: str) -> Optional[float]:
    """Extracts and cleans numeric data from nested API responses."""
    try:
        value = data.get('data', {}).get(key)
        return float(value) if value is not None else None
    except (ValueError, TypeError, AttributeError):
        return None

def calculate_percentage_change(current: float, previous: float) -> float:
    """Computes percentage difference between two price points."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100