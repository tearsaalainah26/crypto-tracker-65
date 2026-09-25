import re
from typing import Any, Dict

# Common patterns for crypto validation
SYMBOL_PATTERN = re.compile(r"^[A-Z0-9]{2,10}$")
EVM_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def validate_symbol(symbol: Any) -> bool:
    """Validates if the ticker symbol is valid (e.g., BTC, ETH)."""
    if not isinstance(symbol, str):
        return False
    return bool(SYMBOL_PATTERN.match(symbol.strip().upper()))


def validate_wallet_address(address: Any) -> bool:
    """Validates if the string is a valid EVM wallet address."""
    if not isinstance(address, str):
        return False
    return bool(EVM_ADDRESS_PATTERN.match(address.strip()))


def validate_transaction_payload(payload: Dict[str, Any]) -> bool:
    """Validates transaction payload in the processing loop."""
    if not isinstance(payload, dict):
        return False

    required_fields = ["symbol", "amount", "price", "wallet"]
    if not all(field in payload for field in required_fields):
        return False

    symbol = payload.get("symbol")
    amount = payload.get("amount")
    price = payload.get("price")
    wallet = payload.get("wallet")

    if not validate_symbol(symbol):
        return False

    if not validate_wallet_address(wallet):
        return False

    try:
        val_amount = float(amount) if amount is not None else -1.0
        val_price = float(price) if price is not None else -1.0
        if val_amount <= 0 or val_price <= 0:
            return False
    except (ValueError, TypeError):
        return False

    return True
