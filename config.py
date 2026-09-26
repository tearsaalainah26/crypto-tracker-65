import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "currency": "usd",
    "update_interval_seconds": 60,
    "tracked_symbols": ["btc", "eth", "sol"],
    "api_base_url": "https://api.coingecko.com/api/v3",
    "alert_threshold_percent": 5.0,
    "max_retries": 3,
    "log_level": "INFO",
}


class ConfigLoader:
    """Loads application configuration with fallback to default values."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Load configuration from JSON file and environment variables."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load {self.config_path}: {err}")

        self._apply_env_overrides()
        return self._config

    def _apply_env_overrides(self) -> None:
        """Override settings with CRYPTO_TRACKER_* environment variables."""
        prefix = "CRYPTO_TRACKER_"
        for key in self._config:
            env_var = f"{prefix}{key.upper()}"
            if env_var in os.environ:
                raw_val = os.environ[env_var]
                default_type = type(DEFAULT_CONFIG[key])
                if default_type is int:
                    self._config[key] = int(raw_val)
                elif default_type is float:
                    self._config[key] = float(raw_val)
                elif default_type is list:
                    self._config[key] = [s.strip() for s in raw_val.split(",")]
                else:
                    self._config[key] = raw_val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self._config.get(key, default)

    @property
    def settings(self) -> Dict[str, Any]:
        """Return a copy of current active configuration."""
        return self._config.copy()
