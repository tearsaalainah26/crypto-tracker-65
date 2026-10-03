import re

class CryptoValidator:
    """Input validation logic for crypto-tracker-65 inputs."""

    SYMBOL_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')

    @staticmethod
    def validate_ticker(ticker: str) -> bool:
        """Verify ticker symbol matches expected format."""
        if not isinstance(ticker, str):
            return False
        return bool(CryptoValidator.SYMBOL_PATTERN.match(ticker.strip().upper()))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Ensure investment amount is positive."""
        try:
            value = float(amount)
            return value > 0
        except (ValueError, TypeError):
            return False

def process_input(ticker: str, amount: float):
    """Main loop entry for input validation."""
    if not CryptoValidator.validate_ticker(ticker):
        raise ValueError(f"Invalid ticker format: {ticker}")
    
    if not CryptoValidator.validate_amount(amount):
        raise ValueError(f"Invalid amount: {amount}. Must be positive.")
    
    return True