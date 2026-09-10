from typing import Optional

class CryptoTrackerError(Exception):
    """Base exception for all crypto-tracker-65 operations."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when the crypto exchange API is unreachable."""
    def __init__(self, message: str, status_code: Optional[int] = None) -> None:
        super().__init__(message)
        self.status_code = status_code

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API request frequency limits are reached."""
    def __init__(self, retry_after: int = 60) -> None:
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after} seconds.")

class ConfigurationError(CryptoTrackerError):
    """Raised when essential config values are missing or invalid."""
    pass

class ValidationError(CryptoTrackerError):
    """Raised when asset data fails format validation."""
    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(f"Validation failed for {field}: {reason}")