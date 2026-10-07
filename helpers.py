from typing import Union, List

def format_price(value: Union[int, float], currency: str = "USD") -> str:
    """Formats a numeric price value into a human-readable currency string."""
    if value is None:
        return "$0.00"
    
    # Display more decimals for low-value micro-cap tokens
    if value < 0.01:
        return f"{value:.8f} {currency.upper()}"
    if value < 1.0:
        return f"{value:.4f} {currency.upper()}"
    return f"${value:,.2f} {currency.upper()}"

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculates the percentage change between two price points safely."""
    if not old_price or old_price == 0:
        return 0.0
    return round(((new_price - old_price) / old_price) * 100.0, 2)

def meets_volatility_threshold(old_price: float, new_price: float, threshold: float) -> bool:
    """Determines if the absolute price change percentage exceeds a threshold."""
    change = calculate_percentage_change(old_price, new_price)
    return abs(change) >= threshold

def chunk_symbols(symbols: List[str], batch_size: int = 50) -> List[List[str]]:
    """Chunks a list of symbols to prevent hitting URI limit on batch requests."""
    return [symbols[i:i + batch_size] for i in range(0, len(symbols), batch_size)]
