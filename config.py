import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "currency": "usd",
    "debug": False
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                print(f"Warning: Could not load {self.config_path}, using defaults")

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]

# Global config instance for crypto-tracker-65
config = ConfigLoader()