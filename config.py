import os
import logging
from typing import Any, Dict

# crypto-tracker-65 global configuration

def get_env_variable(key: str, default: Any = None) -> Any:
    """Retrieves environment variable with validation."""
    try:
        value = os.getenv(key)
        if value is None:
            if default is not None:
                return default
            raise ValueError(f"Missing required environment variable: {key}")
        return value
    except Exception as e:
        logging.error(f"Config retrieval error for {key}: {e}")
        raise

class Config:
    def __init__(self):
        try:
            self.API_KEY = get_env_variable("CRYPTO_API_KEY")
            self.POLLING_INTERVAL = int(get_env_variable("POLLING_INTERVAL", 60))
            self.TIMEOUT = float(get_env_variable("REQUEST_TIMEOUT", 5.0))
        except (ValueError, TypeError) as e:
            logging.critical(f"Invalid configuration types: {e}")
            raise

    def to_dict(self) -> Dict[str, Any]:
        return {
            "api_key_set": bool(self.API_KEY),
            "interval": self.POLLING_INTERVAL,
            "timeout": self.TIMEOUT
        }

# Singleton configuration instance
try:
    settings = Config()
except Exception:
    settings = None