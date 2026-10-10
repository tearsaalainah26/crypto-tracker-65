import re

# crypto-tracker-65 input validation rules
VALID_TICKER_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')
MAX_API_LIMIT = 100

def validate_ticker(ticker: str) -> bool:
    """verify crypto ticker format requirements."""
    if not isinstance(ticker, str):
        return False
    return bool(VALID_TICKER_PATTERN.match(ticker.upper()))

def validate_limit(limit: int) -> bool:
    """ensure api fetch limits remain reasonable."""
    if not isinstance(limit, int):
        return False
    return 1 <= limit <= MAX_API_LIMIT

def sanitize_input(user_input: str) -> str:
    """strip whitespace and convert to upper case."""
    return str(user_input).strip().upper()
