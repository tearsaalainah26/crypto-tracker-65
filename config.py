import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigLoader:
    """Configuration loader with defaults for crypto tracker."""

    DEFAULTS = {
        "api_key": "",
        "exchange": "binance",
        "base_url": "https://api.binance.com/api/v3",
        "tracked_assets": ["BTCUSDT", "ETHUSDT", "SOLUSDT"],
        "poll_interval": 30,
        "alert_threshold": 5.0,
        "log_level": "INFO",
        "cache_ttl": 300,
    }

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = Path(config_path or "config.json")
        self.config: Dict[str, Any] = self.DEFAULTS.copy()
        self._load_from_file()
        self._load_from_env()

    def _load_from_file(self) -> None:
        if self.config_path.exists():
            try:
                with self.config_path.open("r") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        self.config.update(user_config)
            except (json.JSONDecodeError, OSError) as exc:
                # Use defaults if file is invalid
                pass

    def _load_from_env(self) -> None:
        prefix = "CRYPTO_"
        for key in self.DEFAULTS:
            env_var = prefix + key.upper()
            if env_var in os.environ:
                value = os.environ[env_var]
                orig = self.DEFAULTS[key]
                if isinstance(orig, bool):
                    value = value.lower() in ("true", "1", "yes")
                elif isinstance(orig, int):
                    try:
                        value = int(value)
                    except ValueError:
                        continue
                elif isinstance(orig, float):
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                self.config[key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        return self.config.copy()

    def update(self, updates: Dict[str, Any]) -> None:
        self.config.update(updates)

    def save(self) -> bool:
        try:
            with self.config_path.open("w") as f:
                json.dump(self.config, f, indent=2)
            return True
        except OSError:
            return False