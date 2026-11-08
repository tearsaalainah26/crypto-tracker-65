import re
from typing import Any, Optional

# crypto-tracker-65 validation constants
ADDRESS_PATTERN = re.compile(r'^[a-zA-Z0-9]{26,42}$')
SUPPORTED_ASSETS = {'BTC', 'ETH', 'SOL', 'DOT', 'ADA'}

def validate_wallet_address(address: str) -> bool:
    """verify crypto wallet address format"""
    return bool(ADDRESS_PATTERN.match(address))

def validate_ticker(ticker: str) -> bool:
    """check ticker against supported assets list"""
    return ticker.upper() in SUPPORTED_ASSETS

def validate_price_input(value: Any) -> float:
    """sanitization of float values from inputs"""
    try:
        price = float(value)
        if price < 0:
            raise ValueError('negative price provided')
        return price
    except (TypeError, ValueError):
        return 0.0

def sanitize_payload(data: dict) -> dict:
    """filter incoming dictionary keys"""
    allowed = {'symbol', 'amount', 'timestamp'}
    return {k: v for k, v in data.items() if k in allowed}