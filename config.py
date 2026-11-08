import os
from functools import lru_cache

class Settings:
    """
    Configuration management with cached lookups for
    performance-critical settings in crypto-tracker-65.
    """
    def __init__(self):
        self.env = os.getenv("APP_ENV", "production")
        self.api_key = os.getenv("CRYPTO_API_KEY", "")
        self.rate_limit = int(os.getenv("RATE_LIMIT", 100))

    @lru_cache(maxsize=32)
    def get_market_endpoint(self, base_currency: str) -> str:
        """
        Cached endpoint resolution to avoid repeated string formatting
        during high-frequency data ingestion cycles.
        """
        endpoints = {
            "btc": "https://api.exchange.com/v1/ticker/btc",
            "eth": "https://api.exchange.com/v1/ticker/eth",
            "sol": "https://api.exchange.com/v1/ticker/sol"
        }
        return endpoints.get(base_currency.lower(), "https://api.exchange.com/v1/ticker/default")

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Singleton accessor for settings with memoization
    to eliminate redundant instantiation overhead.
    """
    return Settings()