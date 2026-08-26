import logging
from decimal import Decimal, InvalidOperation

logger = logging.getLogger("crypto-tracker-65")

def format_currency(amount: float, currency_symbol: str = "$") -> str:
    """Format a numeric amount into a standard currency string."""
    try:
        dec_amount = Decimal(str(amount))
        return f"{currency_symbol}{dec_amount:,.2f}"
    except (InvalidOperation, TypeError) as e:
        logger.error(f"Failed to format currency for value {amount}: {e}")
        return f"{currency_symbol}0.00"

def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculate the percentage change between two price points."""
    if old_value == 0:
        return 0.0
    try:
        old_dec = Decimal(str(old_value))
        new_dec = Decimal(str(new_value))
        change = ((new_dec - old_dec) / old_dec) * Decimal("100")
        return float(change.quantize(Decimal("0.01")))
    except (InvalidOperation, TypeError) as e:
        logger.error(f"Failed to calculate percentage change: {e}")
        return 0.0

def sanitize_symbol(symbol: str) -> str:
    """Clean and normalize a cryptocurrency trading symbol."""
    if not isinstance(symbol, str):
        return ""
    return symbol.strip().upper()
