import os
from typing import Dict, Any

class Config:
    """Configuration settings for crypto-tracker-65 application."""

    def __init__(self) -> None:
        self.api_key: str = os.getenv("CRYPTO_API_KEY", "default_key")
        self.base_url: str = "https://api.coingecko.com/api/v3"
        self.request_timeout: int = 30
        self.refresh_interval: int = 60

    def get_headers(self) -> Dict[str, str]:
        """Return authentication headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    @classmethod
    def validate_env(cls) -> bool:
        """Ensure required environment variables are present."""
        required_vars: list[str] = ["CRYPTO_API_KEY"]
        return all(os.getenv(var) is not None for var in required_vars)

    def to_dict(self) -> Dict[str, Any]:
        """Export configuration as a dictionary."""
        return {
            "api_key": self.api_key,
            "base_url": self.base_url,
            "timeout": self.request_timeout,
            "interval": self.refresh_interval
        }

app_config: Config = Config()