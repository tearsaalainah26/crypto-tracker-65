"""
Custom exceptions for the crypto-tracker-65 application.
Defines specific error types for API failures, rate limits, and validation.
"""

class CryptoTrackerError(Exception):
    """Base exception class for all crypto tracker errors."""
    pass


class APIConnectionError(CryptoTrackerError):
    """Raised when the application fails to connect to the crypto API provider."""
    def __init__(self, message: str = "Failed to connect to the cryptocurrency API"):
        super().__init__(message)


class RateLimitExceededError(APIConnectionError):
    """Raised when the API request rate limit has been exceeded."""
    def __init__(self, retry_after: int = None):
        message = "Rate limit exceeded."
        if retry_after:
            message += f" Please retry after {retry_after} seconds."
        super().__init__(message)
        self.retry_after = retry_after


class InvalidTickerError(CryptoTrackerError):
    """Raised when a requested cryptocurrency ticker is invalid or unsupported."""
    def __init__(self, ticker: str):
        self.ticker = ticker
        super().__init__(f"The cryptocurrency ticker '{ticker}' is not supported.")


class CacheMissError(CryptoTrackerError):
    """Raised when requested historical data is missing from the local cache."""
    pass
