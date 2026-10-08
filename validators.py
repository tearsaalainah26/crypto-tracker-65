import re

# crypto-tracker-65 input validation utilities

def validate_symbol(symbol: str) -> bool:
    """verify crypto ticker format (e.g., BTC, ETH, SOL)."""
    if not isinstance(symbol, str):
        return False
    return bool(re.match(r"^[A-Z0-9]{2,10}$", symbol))

def validate_amount(amount: str) -> bool:
    """ensure amount is a positive numeric string."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_input(raw_symbol: str, raw_amount: str):
    """main validation gate for user inputs."""
    symbol = raw_symbol.upper().strip()
    
    if not validate_symbol(symbol):
        raise ValueError(f"Invalid ticker symbol: {raw_symbol}")
        
    if not validate_amount(raw_amount):
        raise ValueError(f"Invalid amount: {raw_amount}")
        
    return symbol, float(raw_amount)