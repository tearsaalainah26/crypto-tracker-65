import enum
from typing import Final

# caching constants for ticker operations
CACHE_TTL: Final[int] = 300
MAX_RETRIES: Final[int] = 3
REQUEST_TIMEOUT: Final[float] = 10.0

# supported trading pairs
SUPPORTED_PAIRS: Final[list[str]] = [
    "BTC-USD",
    "ETH-USD",
    "SOL-USD",
    "ADA-USD"
]

class ExchangeStatus(enum.IntEnum):
    OPERATIONAL = 1
    MAINTENANCE = 2
    DISCONNECTED = 3

# connection pool limits for performance
MAX_CONCURRENT_REQUESTS: Final[int] = 10
API_RATE_LIMIT_DELAY: Final[float] = 0.5

def get_cache_key(pair: str) -> str:
    """generate standardized cache key"""
    return f"ticker:{pair.lower()}"