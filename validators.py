import re
from typing import Any, Dict


def is_valid_eth_address(address: str) -> bool:
    """Validate Ethereum wallet address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_btc_address(address: str) -> bool:
    """Validate legacy, P2SH, and Bech32 Bitcoin address formats."""
    if not isinstance(address, str):
        return False
    legacy_or_p2sh = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    bech32 = r"^bc1[a-zA-Z0-9]{8,87}$"
    return bool(re.match(legacy_or_p2sh, address) or re.match(bech32, address, re.IGNORECASE))


def is_valid_symbol(symbol: str) -> bool:
    """Validate cryptocurrency ticker symbol format (e.g., BTC, ETH, BTC/USDT)."""
    if not isinstance(symbol, str):
        return False
    return bool(re.match(r"^[A-Z0-9]{2,10}(/[A-Z0-9]{2,10})?$", symbol.upper()))


def validate_price_alert_config(config: Dict[str, Any]) -> bool:
    """Validate price alert payload structure and values."""
    if not isinstance(config, dict):
        return False

    required_keys = {"symbol", "target_price", "condition"}
    if not required_keys.issubset(config.keys()):
        return False

    if not is_valid_symbol(str(config["symbol"])): 
        return False

    try:
        price = float(config["target_price"])
        if price <= 0:
            return False
    except (ValueError, TypeError):
        return False

    if config["condition"] not in ("above", "below"):
        return False

    return True
