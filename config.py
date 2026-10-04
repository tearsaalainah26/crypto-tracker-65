import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "api_provider": "coingecko",
    "api_key": "",
    "base_currency": "usd",
    "update_interval": 60,
    "request_timeout": 10,
    "tracked_symbols": ["btc", "eth", "sol"],
    "enable_alerts": True,
    "price_alert_threshold_pct": 5.0,
}


class Config:
    """Manages application settings with defaults and environment overrides."""

    def __init__(self, config_path: str = "config.json"):
        self.filepath = Path(config_path)
        self._settings = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads settings from JSON file if present and overrides with env vars."""
        if self.filepath.exists():
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    file_settings = json.load(f)
                    self._settings.update(file_settings)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to parse {self.filepath}, using defaults: {err}")

        # Override dynamic or sensitive parameters from environment variables
        if env_api_key := os.getenv("CRYPTO_API_KEY"):
            self._settings["api_key"] = env_api_key
        if env_currency := os.getenv("CRYPTO_BASE_CURRENCY"):
            self._settings["base_currency"] = env_currency.lower()

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._settings.get(key, default)

    def __getitem__(self, item: str) -> Any:
        return self._settings[item]

    def as_dict(self) -> Dict[str, Any]:
        """Return copy of active configuration dictionary."""
        return self._settings.copy()


config = Config()
