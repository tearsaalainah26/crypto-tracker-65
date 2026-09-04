import re

# Validation patterns for crypto tickers and amounts
SYMBOL_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')

def validate_crypto_input(symbol: str, amount: float) -> bool:
    """Ensures input data conforms to expected formats."""
    if not isinstance(symbol, str) or not SYMBOL_PATTERN.match(symbol):
        return False
    
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False
    
    return True

def sanitize_ticker(symbol: str) -> str:
    """Strips whitespace and normalizes ticker case."""
    return str(symbol).strip().upper()

def process_validated_payload(data: dict):
    """Applies validation rules to incoming market payloads."""
    symbol = sanitize_ticker(data.get('symbol', ''))
    amount = data.get('amount', 0)
    
    if not validate_crypto_input(symbol, amount):
        raise ValueError(f"Invalid input payload: {symbol} with {amount}")
    
    return {"symbol": symbol, "amount": float(amount)}