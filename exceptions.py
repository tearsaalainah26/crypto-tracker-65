class CryptoTrackerError(Exception):
    """Base exception for the crypto-tracker-65 package."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when the crypto exchange API is unreachable."""
    def __init__(self, message: str, status_code: int = 503) -> None:
        super().__init__(message)
        self.status_code: int = status_code

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API request frequency limits are reached."""
    def __init__(self, retry_after: int) -> None:
        self.retry_after: int = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after} seconds.")

class DataValidationError(CryptoTrackerError):
    """Raised when parsed exchange data fails schema validation."""
    def __init__(self, field: str, detail: str) -> None:
        self.field: str = field
        self.detail: str = detail
        super().__init__(f"Validation error in {field}: {detail}")

class InsufficientFundsError(CryptoTrackerError):
    """Raised when account balance is too low for trade."""
    def __init__(self, asset: str, required: float) -> None:
        self.asset: str = asset
        self.required: float = required
        super().__init__(f"Insufficient {asset} balance. Need {required}.")