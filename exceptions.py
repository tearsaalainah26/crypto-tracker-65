class CryptoTrackerError(Exception):
    """Base exception for crypto-tracker-65."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when external crypto APIs are unreachable."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API rate limits are hit."""
    pass

class DataValidationError(CryptoTrackerError):
    """Raised when processed crypto data is invalid."""
    pass

class ConfigurationError(CryptoTrackerError):
    """Raised when environment or config settings are invalid."""
    pass

class StorageError(CryptoTrackerError):
    """Raised when database operations fail."""
    pass