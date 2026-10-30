"""Constants and configuration defaults for crypto-tracker-65."""

from typing import Dict, List, Final

# Base API Endpoints
COINGECKO_BASE_URL: Final[str] = "https://api.coingecko.com/api/v3"
BINANCE_BASE_URL: Final[str] = "https://api.binance.com/api/v3"

# Default Tracking Parameters
DEFAULT_CURRENCY: Final[str] = "usd"
DEFAULT_REFRESH_INTERVAL_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3
REQUEST_TIMEOUT_SECONDS: Final[int] = 10

# Supported Cryptocurrency Identifiers
TOP_TRACKED_ASSETS: Final[List[str]] = [
    "bitcoin",
    "ethereum",
    "solana",
    "cardano",
    "ripple",
    "polkadot",
    "avalanche-2",
]

# Market Data Display Preferences
PRICE_DECIMAL_PLACES: Final[Dict[str, int]] = {
    "usd": 2,
    "eur": 2,
    "gbp": 2,
    "btc": 6,
    "eth": 4,
}

# Cache Duration Settings
CACHE_TTL_PRICES: Final[int] = 15  # seconds
CACHE_TTL_METADATA: Final[int] = 3600  # 1 hour

# Status Identifiers
STATUS_OK: Final[str] = "OK"
STATUS_ERROR: Final[str] = "ERROR"
STATUS_STALE: Final[str] = "STALE"
