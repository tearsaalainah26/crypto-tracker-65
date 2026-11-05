import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "request_timeout_seconds": 10,
    "update_interval_seconds": 60,
    "tracked_assets": ["bitcoin", "ethereum", "solana"],
    "currency": "usd",
    "alert_thresholds": {
        "price_change_percent_24h": 5.0,
        "enable_email_alerts": False,
    },
    "log_level": "INFO",
}


class ConfigLoader:
    """Handles loading and merging application configuration for crypto-tracker."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file and env vars, falling back to defaults."""
        merged_config = DEFAULT_CONFIG.copy()

        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    self._deep_update(merged_config, file_data)
            except (json.JSONDecodeError, IOError) as err:
                print(f"Warning: Failed to parse {self.config_path} ({err}). Using defaults.")

        if env_currency := os.getenv("CRYPTO_CURRENCY"):
            merged_config["currency"] = env_currency.lower()

        if env_interval := os.getenv("UPDATE_INTERVAL"):
            try:
                merged_config["update_interval_seconds"] = int(env_interval)
            except ValueError:
                pass

        self.config = merged_config
        return self.config

    def _deep_update(self, original: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Recursively update nested dictionary configuration."""
        for key, value in update.items():
            if isinstance(value, dict) and key in original and isinstance(original[key], dict):
                self._deep_update(original[key], value)
            else:
                original[key] = value


def get_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Utility helper to load and retrieve configuration dictionary."""
    loader = ConfigLoader(config_path)
    return loader.load_config()
