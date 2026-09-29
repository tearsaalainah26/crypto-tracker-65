import re

# crypto-tracker-65 input validation logic

def validate_ticker(ticker: str) -> bool:
    """Validate cryptocurrency ticker format (e.g., BTC, ETH)."""
    if not ticker or not isinstance(ticker, str):
        return False
    return bool(re.match(r'^[A-Z0-9]{2,10}$', ticker.upper()))

def validate_amount(amount: str) -> bool:
    """Verify input string is a valid positive float."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_user_input(ticker: str, amount: str) -> dict:
    """Sanitize and validate crypto portfolio update inputs."""
    is_valid = validate_ticker(ticker) and validate_amount(amount)
    
    return {
        "status": is_valid,
        "ticker": ticker.upper() if is_valid else None,
        "amount": float(amount) if is_valid else 0.0
    }

def process_input_stream(raw_data: list) -> list:
    """Process bulk inputs and filter invalid data entries."""
    cleaned_data = []
    for item in raw_data:
        result = validate_user_input(item.get('ticker', ''), item.get('amount', '0'))
        if result["status"]:
            cleaned_data.append(result)
    return cleaned_data