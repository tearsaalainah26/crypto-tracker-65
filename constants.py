import os

# API configuration defaults
BASE_URL = "https://api.coingecko.com/api/v3"
REQUEST_TIMEOUT = 10

# Supported crypto asset identifiers
SUPPORTED_ASSETS = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana",
    "ada": "cardano"
}

# Application settings
DEFAULT_CURRENCY = "usd"
UPDATE_INTERVAL_SECONDS = 60

# Environment-based logging settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "crypto_tracker.log"

# Retry policy constants
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5
