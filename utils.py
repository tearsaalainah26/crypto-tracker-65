from typing import Dict, Any, Optional

def format_currency(value: float, currency: str = "USD") -> str:
    """Formats a numeric value into a localized currency string representation."""
    if currency.upper() == "USD":
        if value >= 1.0:
            return f"${value:,.2f}"
        return f"${value:,.6f}"
    return f"{value:,.4f} {currency.upper()}"

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculates the percentage change between two numeric price points."""
    if old_price <= 0:
        return 0.0
    change = ((new_price - old_price) / old_price) * 100
    return round(change, 2)

def extract_market_data(raw_data: Dict[str, Any]) -> Dict[str, Optional[float]]:
    """Extracts and normalizes raw cryptocurrency price data from external payloads."""
    cleaned_data = {}
    for asset_id, market_info in raw_data.items():
        price = market_info.get("usd")
        cleaned_data[asset_id] = float(price) if price is not None else None
    return cleaned_data