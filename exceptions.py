class CryptoTrackerError(Exception):
    """Base exception for the crypto-tracker-65 application."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when the crypto exchange API is unreachable."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API rate limits are hit."""
    pass

class DataValidationError(CryptoTrackerError):
    """Raised when incoming market data is malformed."""
    pass

class ConfigurationError(CryptoTrackerError):
    """Raised when environmental variables are missing or invalid."""
    pass

class DatabaseError(CryptoTrackerError):
    """Raised when database interactions fail."""
    pass