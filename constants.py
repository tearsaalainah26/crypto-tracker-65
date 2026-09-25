import os
from typing import Final

# Network and API settings
API_BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3'
DEFAULT_TIMEOUT: Final[int] = 10

# Supported cryptocurrency tickers
SUPPORTED_COINS: Final[list[str]] = ['bitcoin', 'ethereum', 'solana', 'cardano']

# Storage and path configuration
DATA_DIR: Final[str] = os.getenv('CRYPTO_DATA_DIR', './data')
LOG_FILE: Final[str] = os.path.join(DATA_DIR, 'crypto_tracker.log')

# Refresh intervals in seconds
UPDATE_INTERVAL: Final[int] = 60
RATE_LIMIT_DELAY: Final[float] = 1.5

# Logging format
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Default HTTP headers
HEADERS: Final[dict[str, str]] = {
    'Accept': 'application/json',
    'User-Agent': 'crypto-tracker-65/1.0'
}