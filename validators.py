import re
import math
from typing import Any

class CryptoValidationError(Exception):
    """Custom exception raised when crypto data validation fails."""
    pass


def validate_symbol(symbol: Any) -> str:
    """Validate and normalize a cryptocurrency trading pair or symbol."""
    if not symbol or not isinstance(symbol, str):
        raise CryptoValidationError("Symbol must be a non-empty string")
    
    cleaned = symbol.strip().upper()
    if not re.match(r"^[A-Z0-9]{2,10}(/[A-Z0-9]{2,10})?$", cleaned):
        raise CryptoValidationError(f"Invalid symbol format: {symbol}")
    
    return cleaned


def validate_amount(amount: Any, allow_zero: bool = False) -> float:
    """Validate numeric values for prices, volumes, and balances edge cases."""
    if amount is None:
        raise CryptoValidationError("Amount cannot be None")
        
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise CryptoValidationError(f"Cannot convert '{amount}' to a numeric amount")

    if math.isnan(val) or math.isinf(val):
        raise CryptoValidationError("Amount cannot be NaN or Infinite")

    if val < 0:
        raise CryptoValidationError("Amount cannot be negative")

    if not allow_zero and val == 0:
        raise CryptoValidationError("Amount must be greater than zero")

    return val


def validate_address(address: Any, chain: str = "ETH") -> str:
    """Basic format validation for crypto wallet addresses across supported chains."""
    if not address or not isinstance(address, str):
        raise CryptoValidationError("Wallet address must be a non-empty string")

    addr = address.strip()
    chain_upper = chain.upper()
    
    if chain_upper == "ETH":
        if not re.match(r"^0x[a-fA-F0-9]{40}$", addr):
            raise CryptoValidationError(f"Invalid Ethereum address format: {address}")
    elif chain_upper == "BTC":
        if not re.match(r"^(1|3|bc1)[a-zA-1-9]{25,59}$", addr):
            raise CryptoValidationError(f"Invalid Bitcoin address format: {address}")
    else:
        if len(addr) < 10 or len(addr) > 100:
            raise CryptoValidationError(f"Invalid generic address length for chain {chain}")

    return addr