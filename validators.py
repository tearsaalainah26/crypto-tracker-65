from typing import Any, Dict, Optional

def validate_crypto_data(data: Dict[str, Any]) -> bool:
    """
    Ensures dictionary contains valid cryptocurrency pricing schema.
    Checks for mandatory keys and positive numeric types.
    """
    required_keys = ['symbol', 'price', 'volume']
    
    if not isinstance(data, dict):
        return False

    # Validate mandatory structure
    if not all(key in data for key in required_keys):
        return False

    # Validate numeric types and ranges
    try:
        if not isinstance(data['symbol'], str):
            return False
        
        price = float(data['price'])
        volume = float(data['volume'])
        
        return price >= 0 and volume >= 0
    except (TypeError, ValueError):
        return False

def sanitize_symbol(symbol: Any) -> Optional[str]:
    """
    Standardizes crypto ticker symbols to uppercase.
    """
    if not isinstance(symbol, str):
        return None
        
    clean_symbol = symbol.strip().upper()
    return clean_symbol if len(clean_symbol) <= 10 else None