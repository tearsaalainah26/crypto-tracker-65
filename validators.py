import re

# crypto-tracker-65 input validation constraints
SUPPORTED_TICKERS = {'BTC', 'ETH', 'SOL', 'ADA', 'DOT'}
MIN_AMOUNT = 0.00000001
MAX_AMOUNT = 1000000.0

def validate_ticker(ticker: str) -> bool:
    """verify if the ticker is within the supported list"""
    return ticker.upper() in SUPPORTED_TICKERS

def validate_amount(amount: float) -> bool:
    """ensure amount is positive and within logical trading bounds"""
    return MIN_AMOUNT <= amount <= MAX_AMOUNT

def validate_address(address: str) -> bool:
    """regex check for basic wallet address structure"""
    pattern = r'^(0x)?[0-9a-fA-F]{40}$'
    return bool(re.match(pattern, address))

def sanitize_input(user_input: str) -> str:
    """strip whitespace and enforce uppercase for consistency"""
    return user_input.strip().upper()
