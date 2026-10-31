"""Validation utilities for cryptocurrency wallet addresses and market pairs."""

import re
from typing import Dict, Pattern

# Pre-compiled regex patterns for common crypto address formats
ADDRESS_PATTERNS: Dict[str, Pattern[str]] = {
    "BTC": re.compile(r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-09]{38,59})$"),
    "ETH": re.compile(r"^0x[a-fA-F0-9]{40}$"),
    "SOL": re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"),
}

PAIR_PATTERN: Pattern[str] = re.compile(r"^[A-Z0-9]{2,10}/[A-Z0-9]{2,10}$")


def validate_wallet_address(address: str, chain: str) -> bool:
    """Validate if a crypto wallet address matches the target blockchain format.

    Args:
        address: The public wallet address string to check.
        chain: Ticker symbol of the blockchain network (e.g., 'BTC', 'ETH', 'SOL').

    Returns:
        True if the address matches the pattern for the specified chain, False otherwise.
    """
    pattern = ADDRESS_PATTERNS.get(chain.upper())
    if not pattern:
        return False
    return bool(pattern.match(address.strip()))


def validate_symbol_pair(pair: str) -> bool:
    """Verify that a trading pair string follows standard formatting (e.g., BTC/USD).

    Args:
        pair: Standardized market pair notation string.

    Returns:
        True if valid format, False otherwise.
    """
    if not pair or not isinstance(pair, str):
        return False
    return bool(PAIR_PATTERN.match(pair.strip().upper()))


def validate_price_alert(target_price: float, current_price: float) -> bool:
    """Ensure price alert trigger values are positive and mathematically valid.

    Args:
        target_price: Desired price trigger threshold.
        current_price: Current market price of the asset.

    Returns:
        True if prices are positive numbers and non-zero.
    """
    if target_price <= 0 or current_price <= 0:
        return False
    return True
