import logging
from typing import Final, Dict

# performance-critical constants cached for memory efficiency

CACHE_TTL_SECONDS: Final[int] = 300
API_RATE_LIMIT_PER_MINUTE: Final[int] = 60

# mapping of crypto pairs to internal processing IDs
# dictionary lookups provide o(1) performance
SYMBOL_MAP: Final[Dict[str, int]] = {
    "BTC/USD": 1,
    "ETH/USD": 2,
    "SOL/USD": 3,
    "ADA/USD": 4,
    "DOT/USD": 5,
    "MATIC/USD": 6,
    "LINK/USD": 7,
    "XRP/USD": 8,
    "DOGE/USD": 9,
    "AVAX/USD": 10
}

# internal worker thread configurations
MAX_WORKER_THREADS: Final[int] = 8
BATCH_SIZE: Final[int] = 100

def get_logger(name: str) -> logging.Logger:
    """standardized logger instance configuration"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger