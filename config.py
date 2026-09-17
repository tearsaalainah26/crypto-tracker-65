import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.crypto-tracker-65.com",
    "refresh_rate": 60,
    "currency": "USD",
    "retries": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file or return defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load {config_path}: {e}")
    
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Retrieve specific setting from global state."""
    config = load_config()
    return config.get(key, default)