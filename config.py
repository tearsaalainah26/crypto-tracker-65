import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "log_level": "INFO",
    "symbols": ["bitcoin", "ethereum"]
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with defaults as fallback."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {config_path}: {e}")
    
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Helper to retrieve a specific configuration key."""
    cfg = load_config()
    return cfg.get(key, default)

if __name__ == "__main__":
    # Example usage for crypto-tracker-65
    current_cfg = load_config()
    print(f"Loaded configuration: {current_cfg}")