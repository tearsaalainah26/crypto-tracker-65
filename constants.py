from typing import Final

# Crypto asset configuration
SUPPORTED_ASSETS: Final[list[str]] = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT']

# Network and API constants
DEFAULT_TIMEOUT: Final[int] = 10
API_BASE_URL: Final[str] = 'https://api.crypto-tracker-65.com/v1'
MAX_RETRIES: Final[int] = 3

# Formatting constants
CURRENCY_SYMBOL: Final[str] = '$'
DECIMAL_PRECISION: Final[int] = 8

# Application settings
POLLING_INTERVAL_SECONDS: Final[int] = 60
DEFAULT_DB_PATH: Final[str] = 'crypto_data.db'

def get_asset_limit(asset: str) -> float:
    """Return maximum order limit for a specific asset."""
    limits = {
        'BTC': 1.0,
        'ETH': 10.0,
        'SOL': 100.0,
        'ADA': 10000.0,
        'DOT': 500.0
    }
    return limits.get(asset, 0.0)

def format_price(value: float) -> str:
    """Format currency values consistently across the app."""
    return f"{CURRENCY_SYMBOL}{value:.2f}"