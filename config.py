import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_base_url": "https://api.crypto-tracker-65.com",
    "refresh_interval": 60,
    "currency": "USD",
    "max_retries": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with defaults fallbacks."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

if __name__ == "__main__":
    # Example usage for crypto-tracker-65
    current_cfg = load_config()
    print(f"Active config: {current_cfg}")