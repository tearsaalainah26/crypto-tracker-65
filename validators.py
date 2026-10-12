import re

class InputValidator:
    """Validator for cryptocurrency tracking input parameters."""

    # Regex for common crypto symbols (2-5 uppercase chars)
    SYMBOL_PATTERN = re.compile(r'^[A-Z]{2,5}$')

    @staticmethod
    def validate_ticker(ticker: str) -> bool:
        """Verify if the ticker format is acceptable."""
        return bool(InputValidator.SYMBOL_PATTERN.match(ticker.upper()))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Ensure the trade amount is a positive number."""
        try:
            val = float(amount)
            return val > 0
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_fiat(currency: str) -> bool:
        """Check if fiat code is standard 3-letter format."""
        return isinstance(currency, str) and len(currency) == 3

def process_input(data: dict):
    """Main validation routine for crypto trade data."""
    required = ['ticker', 'amount', 'fiat']
    
    # Ensure all keys exist
    if not all(k in data for k in required):
        return False

    # Run individual field checks
    if not InputValidator.validate_ticker(data['ticker']):
        return False
    if not InputValidator.validate_amount(data['amount']):
        return False
    if not InputValidator.validate_fiat(data['fiat']):
        return False

    return True