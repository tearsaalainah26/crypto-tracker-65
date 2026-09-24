"""System-wide constants and default configurations for crypto tracking."""

from typing import Dict, List, Final

# Supported API Endpoints
DEFAULT_API_BASE_URL: Final[str] = "https://api.coingecko.com/api/v3"
BINANCE_API_BASE_URL: Final[str] = "https://api.binance.com/api/v3"

# Default fetch settings
DEFAULT_CURRENCY: Final[str] = "usd"
DEFAULT_TIMEOUT_SECONDS: Final[int] = 10
MAX_RETRIES: Final[int] = 3

# Standard tracking pairs
POPULAR_TRACKING_PAIRS: Final[List[str]] = [
    "bitcoin",
    "ethereum",
    "solana",
    "cardano",
    "polkadot",
    "ripple",
]

# Valid timeframes for historical data fetch
VALID_TIMEFRAMES: Final[Dict[str, str]] = {
    "1d": "1",
    "7d": "7",
    "14d": "14",
    "30d": "30",
    "90d": "90",
    "1y": "365",
    "max": "max",
}

# HTTP Status and Error Messages
RATE_LIMIT_STATUS_CODE: Final[int] = 429
ERROR_MESSAGES: Final[Dict[str, str]] = {
    "rate_limit": "API rate limit exceeded. Please wait before retrying.",
    "invalid_symbol": "Provided cryptocurrency symbol is not supported.",
    "network_error": "Failed to connect to the remote price feed.",
}


def get_supported_timeframes() -> List[str]:
    """Return list of valid timeframe keys for API queries."""
    return list(VALID_TIMEFRAMES.keys())
