import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "log_level": "INFO",
    "symbols": ["BTC", "ETH", "SOL"]
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from json file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {config_path}: {e}. Using defaults.")
            
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Checks if essential configuration keys are present.
    """
    required_keys = ["api_url", "symbols"]
    return all(key in config for key in required_keys)