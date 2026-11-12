import enum
from typing import Final

# Configuration for crypto-tracker-65 performance optimization
# Using tuple collections for constant time lookups instead of lists

SUPPORTED_ASSETS: Final[tuple[str, ...]] = (
    "BTC", "ETH", "SOL", "ADA", "DOT", "MATIC", "LINK"
)

API_RATE_LIMIT_DELAY: Final[float] = 0.5
CACHE_EXPIRATION_SECONDS: Final[int] = 300

class ExchangeEndpoints(enum.Enum):
    COINGECKO = "https://api.coingecko.com/api/v3"
    BINANCE = "https://api.binance.com/api/v3"

# Pre-computed regex patterns to reduce initialization overhead during processing loops
import re

ASSET_VALIDATION_PATTERN: Final[re.Pattern] = re.compile(r"^[A-Z]{2,5}$")

def get_asset_list() -> tuple[str, ...]:
    """Return the immutable tuple of supported assets."""
    return SUPPORTED_ASSETS