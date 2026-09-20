import os
from typing import Dict, Any

class Config:
    """Centralized configuration management for crypto-tracker-65."""
    
    def __init__(self) -> None:
        self.api_key: str = os.getenv("CRYPTO_API_KEY", "default_key")
        self.base_url: str = "https://api.coingecko.com/api/v3"
        self.refresh_interval: int = 60
        self.supported_assets: list[str] = ["bitcoin", "ethereum", "solana"]

    def get_headers(self) -> Dict[str, str]:
        """Return common request headers for API calls."""
        return {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }

def load_config() -> Config:
    """Factory method for config initialization."""
    return Config()