class CryptoTrackerError(Exception):
    """Base exception for the crypto-tracker-65 application."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when external crypto APIs are unreachable."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when hitting API rate limits."""
    pass

class DataValidationError(CryptoTrackerError):
    """Raised when parsed crypto data is malformed."""
    pass

class ConfigurationError(CryptoTrackerError):
    """Raised when environment variables or config files are missing."""
    pass

def handle_crypto_exception(e: Exception) -> str:
    """Centralized error mapping for logging and UI feedback."""
    if isinstance(e, APIConnectionError):
        return "Network issue: unable to reach crypto exchange."
    if isinstance(e, RateLimitExceeded):
        return "Rate limit hit: please wait before next request."
    if isinstance(e, DataValidationError):
        return "Data error: received invalid format from source."
    return f"Unexpected application error: {str(e)}"