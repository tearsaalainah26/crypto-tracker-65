class CryptoTrackerError(Exception):
    """Base exception for the crypto-tracker-65 application."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when external crypto API connectivity fails."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API request thresholds are reached."""
    pass

class DataParsingError(CryptoTrackerError):
    """Raised when incoming JSON data is malformed."""
    pass

class InvalidCurrencyPairError(CryptoTrackerError):
    """Raised when the requested symbol is not supported."""
    pass

class InsufficientBalanceError(CryptoTrackerError):
    """Raised for trades exceeding available wallet funds."""
    pass

def handle_crypto_exception(e: Exception) -> str:
    """Converts internal exceptions to user-friendly messages."""
    if isinstance(e, RateLimitExceeded):
        return "API limit reached, please retry later."
    if isinstance(e, DataParsingError):
        return "Failed to parse response from market data provider."
    if isinstance(e, InvalidCurrencyPairError):
        return "The requested cryptocurrency pair is currently unavailable."
    return "An unexpected error occurred during data processing."