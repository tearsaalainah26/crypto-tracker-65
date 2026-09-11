import logging

logger = logging.getLogger(__name__)

def validate_ticker(ticker: str) -> bool:
    """Ensures the crypto ticker is alphanumeric and within reasonable length."""
    if not isinstance(ticker, str):
        return False
    if not (1 <= len(ticker) <= 10):
        return False
    return ticker.isalnum()

def validate_amount(amount: float) -> bool:
    """Checks if the trade amount is a positive numerical value."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_input(ticker: str, amount: float) -> dict:
    """Orchestrates validation for incoming data points."""
    if not validate_ticker(ticker):
        logger.error(f"Invalid ticker format: {ticker}")
        return {"status": "error", "message": "invalid ticker"}
    
    if not validate_amount(amount):
        logger.error(f"Invalid amount provided: {amount}")
        return {"status": "error", "message": "invalid amount"}
        
    return {"status": "success", "data": {"ticker": ticker.upper(), "amount": float(amount)}}
