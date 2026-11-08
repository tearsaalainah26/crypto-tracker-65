import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.crypto.com/v1",
    "refresh_interval": 60,
    "log_level": "INFO",
    "tracked_assets": ["BTC", "ETH"]
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns default values."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Helper to retrieve a single setting from the current config."""
    config = load_config()
    return config.get(key, default)

if __name__ == "__main__":
    # Example usage for crypto-tracker-65
    current_cfg = load_config()
    print(f"Active assets: {current_cfg['tracked_assets']}")