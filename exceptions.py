"""Custom exceptions for crypto-tracker-65."""

class CryptoTrackerError(Exception):
    """Base exception for all crypto tracker errors."""
    pass


class APIConnectionError(CryptoTrackerError):
    """Raised when connection to cryptocurrency API fails."""
    def __init__(self, message="Failed to connect to the crypto exchange API."):
        self.message = message
        super().__init__(self.message)


class RateLimitExceededError(CryptoTrackerError):
    """Raised when API rate limit is hit."""
    def __init__(self, retry_after=60, message=None):
        self.retry_after = retry_after
        self.message = message or f"Rate limit exceeded. Retry after {retry_after} seconds."
        super().__init__(self.message)


class InvalidSymbolError(CryptoTrackerError):
    """Raised when an unsupported or invalid crypto symbol is requested."""
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.message = f"The crypto symbol '{symbol}' is invalid or not supported."
        super().__init__(self.message)


class DataParsingError(CryptoTrackerError):
    """Raised when market data payload cannot be parsed."""
    def __init__(self, details: str):
        self.details = details
        self.message = f"Failed to parse incoming crypto data: {details}"
        super().__init__(self.message)
