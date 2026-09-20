import re
from typing import Any, Optional

# Supported cryptocurrency ticker patterns
VALID_TICKER_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')

def validate_ticker(ticker: Any) -> str:
    """Validates that the input is a proper cryptocurrency ticker."""
    if not isinstance(ticker, str):
        raise ValueError(f"Ticker must be a string, got {type(ticker).__name__}")
    
    clean_ticker = ticker.strip().upper()
    if not VALID_TICKER_PATTERN.match(clean_ticker):
        raise ValueError(f"Invalid ticker format: {clean_ticker}")
    
    return clean_ticker

def validate_amount(amount: Any) -> float:
    """Validates that the input is a positive numerical amount."""
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError("Amount must be greater than zero")
        return value
    except (TypeError, ValueError):
        raise ValueError(f"Invalid numeric amount: {amount}")

def validate_input(ticker: Any, amount: Any) -> tuple[str, float]:
    """Main interface for input validation in processing loop."""
    validated_ticker = validate_ticker(ticker)
    validated_amount = validate_amount(amount)
    return validated_ticker, validated_amount