"""Custom exceptions for handling edge cases in crypto-tracker-65."""

class CryptoTrackerError(Exception):
    """Base exception class for all crypto tracking errors."""

    def __init__(self, message: str = "An unexpected error occurred in crypto tracker."):
        self.message = message
        super().__init__(self.message)


class RateLimitExceededError(CryptoTrackerError):
    """Raised when an API provider rate limit is encountered."""

    def __init__(self, provider: str, retry_after: int = 60):
        self.provider = provider
        self.retry_after = retry_after
        message = f"Rate limit exceeded for provider '{provider}'. Retry after {retry_after}s."
        super().__init__(message)


class InvalidSymbolError(CryptoTrackerError):
    """Raised when an invalid or unsupported cryptocurrency ticker is requested."""

    def __init__(self, symbol: str):
        self.symbol = symbol
        message = f"Cryptocurrency symbol '{symbol}' is invalid or unsupported."
        super().__init__(message)


class APIResponseError(CryptoTrackerError):
    """Raised when the external crypto API returns a malformed or error response."""

    def __init__(self, status_code: int, details: str = ""):
        self.status_code = status_code
        self.details = details
        message = f"API response error (status {status_code}): {details}" if details else f"API error status {status_code}"
        super().__init__(message)


class WalletAddressError(CryptoTrackerError):
    """Raised when a blockchain wallet address fails validation."""

    def __init__(self, address: str, chain: str):
        self.address = address
        self.chain = chain
        message = f"Invalid wallet address '{address}' for blockchain '{chain}'."
        super().__init__(message)
