import decimal
from typing import Union, List

def normalize_amount(amount: Union[str, float, int]) -> decimal.Decimal:
    """Converts various input types to a precise decimal for crypto math."""
    return decimal.Decimal(str(amount)).quantize(decimal.Decimal('0.00000001'), rounding=decimal.ROUND_HALF_UP)

def format_currency(value: decimal.Decimal, symbol: str = '$') -> str:
    """Formats decimal crypto balances into human-readable strings."""
    return f"{symbol}{value:,.8f}"

def calculate_percentage_change(old: float, new: float) -> float:
    """Computes price volatility between two data points."""
    if old == 0:
        return 0.0
    return ((new - old) / old) * 100

def chunk_symbols(symbols: List[str], size: int = 50) -> List[List[str]]:
    """Splits large coin lists for API batch requests."""
    return [symbols[i:i + size] for i in range(0, len(symbols), size)]

def sanitize_symbol(symbol: str) -> str:
    """Ensures coin symbols are uppercase and stripped of whitespace."""
    return symbol.strip().upper()