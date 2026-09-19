from typing import Dict, List

# Supported crypto asset pairs
SUPPORTED_PAIRS: List[str] = ['BTC/USD', 'ETH/USD', 'SOL/USD', 'ADA/USD']

# API endpoints for exchange data
EXCHANGE_API_URLS: Dict[str, str] = {
    'binance': 'https://api.binance.com/api/v3/ticker/price',
    'coinbase': 'https://api.coinbase.com/v2/prices',
    'kraken': 'https://api.kraken.com/0/public/Ticker'
}

# Default request timeout in seconds
HTTP_TIMEOUT: int = 10

# Retry configuration
MAX_RETRIES: int = 3
RETRY_BACKOFF_FACTOR: float = 0.5

# Logging configuration
LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL: str = 'INFO'

# Data refresh interval in seconds
REFRESH_INTERVAL: int = 60

# Default currency for calculations
BASE_CURRENCY: str = 'USD'