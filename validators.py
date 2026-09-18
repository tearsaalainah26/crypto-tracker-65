from typing import Union, Optional


def validate_symbol(symbol: str) -> bool:
    """
    Checks if the provided crypto ticker symbol is formatted correctly.
    
    Args:
        symbol: The currency ticker string (e.g., 'BTC').
        
    Returns:
        bool: True if the symbol is uppercase and 3-5 chars long.
    """
    if not isinstance(symbol, str):
        return False
    return 3 <= len(symbol) <= 5 and symbol.isalpha() and symbol.isupper()


def validate_amount(amount: Union[int, float]) -> bool:
    """
    Ensures the trade amount is a positive numerical value.
    
    Args:
        amount: The value to validate.
        
    Returns:
        bool: True if amount is positive and numeric.
    """
    if not isinstance(amount, (int, float)):
        return False
    return amount > 0


def sanitize_pair(base: str, quote: str) -> Optional[str]:
    """
    Constructs a normalized trading pair string.
    
    Args:
        base: Base currency ticker.
        quote: Quote currency ticker.
        
    Returns:
        Normalized pair string or None if inputs are invalid.
    """
    if validate_symbol(base) and validate_symbol(quote):
        return f"{base}/{quote}"
    return None