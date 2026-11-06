import decimal
import datetime
from typing import Union

def format_crypto_amount(value: Union[str, float, int], precision: int = 8) -> decimal.Decimal:
    """Converts raw input to a high-precision decimal for ledger accuracy."""
    return decimal.Decimal(str(value)).quantize(decimal.Decimal('1.' + '0' * precision))

def get_timestamp_iso() -> str:
    """Returns current UTC timestamp in ISO 8601 format for database logs."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def calculate_profit_margin(buy_price: float, sell_price: float) -> float:
    """Calculates percentage difference between entry and exit prices."""
    if buy_price <= 0:
        return 0.0
    return ((sell_price - buy_price) / buy_price) * 100

def validate_ticker_symbol(symbol: str) -> bool:
    """Checks if ticker matches standard uppercase crypto naming convention."""
    return symbol.isupper() and 2 <= len(symbol) <= 6 and symbol.isalpha()