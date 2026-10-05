import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "COIN_GECKO_API_KEY": "",
    "UPDATE_INTERVAL_SECONDS": 60,
    "TRACKED_COINS": ["bitcoin", "ethereum", "solana"],
    "VS_CURRENCY": "usd",
    "LOG_LEVEL": "INFO"
}

class Config:
    """Manages configuration loaded from files and environment variables for the crypto tracker."""
    
    def __init__(self, config_filepath: str = "config.json"):
        self.filepath = config_filepath
        self.settings: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configuration settings, preferring environment variables over JSON file."""
        # Load default settings from local json configuration if present
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    file_settings = json.load(f)
                    self.settings.update(file_settings)
            except (json.JSONDecodeError, OSError):
                # Suppress error and fallback to hardcoded default values
                pass

        # Override settings if environment variables are defined
        for key, default_val in DEFAULT_CONFIG.items():
            env_val = os.getenv(key)
            if env_val is not None:
                if isinstance(default_val, int):
                    try:
                        self.settings[key] = int(env_val)
                    except ValueError:
                        pass
                elif isinstance(default_val, list):
                    try:
                        self.settings[key] = [item.strip() for item in env_val.split(",")]
                    except Exception:
                        pass
                else:
                    self.settings[key] = env_val

    def get(self, key: str) -> Any:
        """Retrieves config value by key falling back to default if absent."""
        return self.settings.get(key, DEFAULT_CONFIG.get(key))