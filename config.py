import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "currency": "usd",
    "timeout": 10
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config file: {e}. Using defaults.")
    
    return config

if __name__ == "__main__":
    # Example usage for crypto-tracker-65
    current_config = load_config()
    print(f"Loaded configuration: {current_config}")