import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "currency": "usd",
    "log_level": "INFO"
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
            print(f"Warning: failed to load config file: {e}. Using defaults.")
            
    return config

def get_setting(key: str, config: Dict[str, Any]) -> Any:
    """Retrieve specific setting with fallback to defaults."""
    return config.get(key, DEFAULT_CONFIG.get(key))