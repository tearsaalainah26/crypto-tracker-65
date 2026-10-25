from typing import Final

# Cache configurations for high-frequency trading data
CACHE_TTL: Final[int] = 60
CACHE_MAX_SIZE: Final[int] = 1024

# Network optimization parameters
REQUEST_TIMEOUT: Final[float] = 5.0
MAX_RETRIES: Final[int] = 3
CONNECTION_POOL_SIZE: Final[int] = 20

# Data processing batch sizes
BATCH_SIZE: Final[int] = 100
CONCURRENT_WORKERS: Final[int] = 4

# Resource limits for memory management
MEMORY_THRESHOLD_MB: Final[int] = 512
GC_COLLECTION_INTERVAL: Final[int] = 300

# API rate limiting
RATE_LIMIT_PER_SECOND: Final[int] = 50
BACKOFF_FACTOR: Final[float] = 1.5