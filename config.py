import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "currency": "usd",
    "max_retries": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file with fallback to hardcoded defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load {config_path}: {e}. Using defaults.")
    
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Retrieve specific configuration value safely."""
    config = load_config()
    return config.get(key, default)