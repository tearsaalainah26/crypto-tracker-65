import re
from typing import Optional

# regex patterns for crypto validation
SYMBOL_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')
ADDRESS_PATTERN = re.compile(r'^[a-zA-Z0-9]{26,42}$')

def validate_symbol(symbol: str) -> bool:
    """verify crypto ticker format"""
    return bool(SYMBOL_PATTERN.match(symbol.upper()))

def validate_address(address: str, chain: str = 'eth') -> bool:
    """check crypto wallet address integrity"""
    if not address or len(address) < 20:
        return False
    return bool(ADDRESS_PATTERN.match(address))

def sanitize_input(user_input: Optional[str]) -> str:
    """strip whitespace and force uppercase"""
    if not user_input:
        return ""
    return user_input.strip().upper()

class ValidationError(Exception):
    """custom exception for validation failures"""
    pass