import re
from typing import Dict, Any, Union

# Regex for standard crypto ticker symbols (2 to 10 alphanumeric characters)
SYMBOL_PATTERN = re.compile(r"^[A-Z0-9]{2,10}$")

def validate_ticker(symbol: str) -> bool:
    """Validates if the ticker symbol conforms to standard crypto formats."""
    if not isinstance(symbol, str):
        return False
    return bool(SYMBOL_PATTERN.match(symbol.upper()))

def validate_price(price: Union[int, float]) -> bool:
    """Ensures the cryptocurrency price is a positive float or int."""
    if not isinstance(price, (int, float)):
        return False
    return price > 0.0

def validate_transaction_payload(payload: Dict[str, Any]) -> bool:
    """
    Validates incoming transaction payloads before processing.
    Expected structure containing symbol, amount, and price.
    """
    if not isinstance(payload, dict):
        return False

    required_keys = {"symbol", "amount", "price"}
    if not required_keys.issubset(payload.keys()):
        return False

    if not validate_ticker(payload["symbol"]):
        return False

    try:
        amount = float(payload["amount"])
        price = float(payload["price"])
        if amount <= 0 or price <= 0:
            return False
    except (ValueError, TypeError):
        return False

    return True
