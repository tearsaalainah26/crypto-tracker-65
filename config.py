import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "primary_currency": "usd",
    "update_interval_seconds": 30,
    "api_endpoints": {
        "coingecko": "https://api.coingecko.com/api/v3",
        "binance": "https://api.binance.com/api/v3",
    },
    "tracked_assets": ["bitcoin", "ethereum", "solana"],
    "request_timeout_seconds": 10,
    "max_retries": 3,
    "enable_cache": True,
}


class ConfigLoader:
    """Loads configuration from environment variables and JSON files with fallback defaults."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration hierarchy: defaults -> file -> environment variables."""
        if self.config_path and self.config_path.is_file():
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    file_config = json.load(file)
                    self._merge_dicts(self._config, file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config file: {err}")

        self._apply_env_overrides()
        return self._config

    def _merge_dicts(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Recursively update target dictionary with source dictionary values."""
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._merge_dicts(target[key], value)
            else:
                target[key] = value

    def _apply_env_overrides(self) -> None:
        """Override configuration parameters using CRYPTO_TRACKER_* environment variables."""
        currency = os.getenv("CRYPTO_TRACKER_CURRENCY")
        if currency:
            self._config["primary_currency"] = currency.lower()

        interval = os.getenv("CRYPTO_TRACKER_INTERVAL")
        if interval and interval.isdigit():
            self._config["update_interval_seconds"] = int(interval)

        timeout = os.getenv("CRYPTO_TRACKER_TIMEOUT")
        if timeout and timeout.isdigit():
            self._config["request_timeout_seconds"] = int(timeout)


def get_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Convenience function to load and return global tracking configuration."""
    loader = ConfigLoader(config_path)
    return loader.load()