import re

# crypto-tracker-65 input validation helpers

def validate_ticker(ticker: str) -> bool:
    """Validates that the ticker symbol is 1-10 uppercase alphanumeric chars."""
    if not isinstance(ticker, str):
        return False
    return bool(re.match(r"^[A-Z0-9]{1,10}$", ticker))

def validate_amount(amount: float) -> bool:
    """Ensures the amount is a positive float for trades."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_request_payload(data: dict) -> bool:
    """Checks payload integrity for crypto-tracker-65 API inputs."""
    required = ['ticker', 'amount']
    if not all(key in data for key in required):
        return False
        
    return (
        validate_ticker(data['ticker']) and 
        validate_amount(data['amount'])
    )

def sanitize_input(value: str) -> str:
    """Basic sanitization for string inputs."""
    if not isinstance(value, str):
        return ""
    return value.strip().upper()