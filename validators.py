import re
from typing import Dict, Any

# Standard validation patterns
SYMBOL_PATTERN = re.compile(r"^[A-Z0-9]{2,10}$")
SUPPORTED_FIAT = {"USD", "EUR", "GBP", "JPY", "CAD"}

def validate_crypto_symbol(symbol: Any) -> str:
    """Validates and normalizes a cryptocurrency symbol (e.g., BTC, ETH)."""
    if not isinstance(symbol, str):
        raise ValueError("Cryptocurrency symbol must be a string value")
    
    cleaned = symbol.strip().upper()
    if not SYMBOL_PATTERN.match(cleaned):
        raise ValueError(f"Invalid symbol format: '{symbol}'. Must be 2-10 alphanumeric characters.")
    return cleaned

def validate_transaction_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validates incoming market data payload in the processing loop."""
    if not isinstance(data, dict):
        raise ValueError("Payload must be a dictionary database entry")

    # Ensure mandatory fields are present
    required_fields = {"symbol", "price", "volume"}
    missing = required_fields - data.keys()
    if missing:
        raise ValueError(f"Missing required fields in payload: {', '.join(missing)}")

    # Validate and clean specific fields
    symbol = validate_crypto_symbol(data["symbol"])

    try:
        price = float(data["price"])
        if price <= 0:
            raise ValueError("Asset price must be a positive float higher than zero")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid numerical price field: {data['price']}") from e

    try:
        volume = float(data["volume"])
        if volume < 0:
            raise ValueError("Asset volume must be a non-negative float value")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid numerical volume field: {data['volume']}") from e

    fiat = str(data.get("fiat", "USD")).strip().upper()
    if fiat not in SUPPORTED_FIAT:
        raise ValueError(f"Unsupported fiat currency: '{fiat}'")

    return {
        "symbol": symbol,
        "price": price,
        "volume": volume,
        "fiat": fiat
    }