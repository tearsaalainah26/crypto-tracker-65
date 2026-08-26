def validate_crypto_symbol(symbol: str) -> bool:
    """
    Validate the cryptocurrency ticker symbol format.
    Ensures it is alphanumeric and between 2 to 10 characters.
    """
    if not isinstance(symbol, str):
        return False
        
    cleaned = symbol.strip().upper()
    if 2 <= len(cleaned) <= 10 and cleaned.isalnum():
        return True
        
    return False


def validate_price_payload(payload: dict) -> bool:
    """
    Validate incoming price data payload from the exchange API.
    Checks for required keys and positive numerical values.
    """
    required_keys = {"symbol", "price", "timestamp"}
    
    if not isinstance(payload, dict):
        return False
        
    if not required_keys.issubset(payload.keys()):
        return False
        
    try:
        price = float(payload["price"])
        timestamp = float(payload["timestamp"])
        
        if price <= 0 or timestamp <= 0:
            return False
    except (ValueError, TypeError):
        return False
        
    return validate_crypto_symbol(payload["symbol"])


def sanitize_input(user_input: str) -> str:
    """
    Sanitize raw user input for safe processing in the tracking loop.
    """
    if not user_input:
        return ""
        
    return "".join(char for char in user_input if char.isalnum() or char in "_-")
