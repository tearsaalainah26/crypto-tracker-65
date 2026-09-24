import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "supported_coins": ["bitcoin", "ethereum", "solana"],
    "log_level": "INFO"
}

class ConfigLoader:
    """Handles loading and merging of crypto-tracker-65 configuration."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load_from_file()

    def _load_from_file(self) -> None:
        """Reads settings from local JSON file if it exists."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Configuration file error: {e}. Using defaults.")

    def get(self, key: str, default: Any = None) -> Any:
        """Returns the value for a given key."""
        return self.settings.get(key, default)

# Global instance for project-wide access
config = ConfigLoader()