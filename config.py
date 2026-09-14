import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "debug_mode": False,
    "tracked_assets": ["bitcoin", "ethereum"]
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config, using defaults: {e}")
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Utility to retrieve a single setting from environment or config."""
    env_val = os.getenv(key.upper())
    if env_val:
        return env_val
    
    config = load_config()
    return config.get(key, default)