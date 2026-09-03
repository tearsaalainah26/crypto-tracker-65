import os
import json
from typing import Any, Dict, List

DEFAULT_CONFIG = {
    "API_KEY": "",
    "BASE_CURRENCY": "USD",
    "UPDATE_INTERVAL_SECONDS": "60",
    "LOG_LEVEL": "INFO",
    "TRACKED_COINS": "bitcoin,ethereum,solana",
    "COINGECKO_API_URL": "https://api.coingecko.com/api/v3"
}

class ConfigLoader:
    def __init__(self, config_file_path: str = "config.json"):
        self.config_file_path = config_file_path
        self.settings: Dict[str, Any] = {}
        self.load_configuration()

    def load_configuration(self) -> None:
        # Initialize settings with hardcoded defaults
        self.settings = DEFAULT_CONFIG.copy()

        # Override with JSON config file if present and valid
        if os.path.exists(self.config_file_path):
            try:
                with open(self.config_file_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        for key, value in file_data.items():
                            self.settings[key.upper()] = str(value)
            except (json.JSONDecodeError, IOError):
                # Fallback to defaults if configuration file is corrupted
                pass

        # Override with environment variables prefixed with CRYPTO_
        for key in DEFAULT_CONFIG:
            env_value = os.environ.get(f"CRYPTO_{key}")
            if env_value is not None:
                self.settings[key] = env_value

    def get_api_key(self) -> str:
        return self.settings.get("API_KEY", "")

    def get_base_currency(self) -> str:
        return self.settings.get("BASE_CURRENCY", "USD").upper()

    def get_update_interval(self) -> int:
        try:
            return int(self.settings.get("UPDATE_INTERVAL_SECONDS", 60))
        except ValueError:
            return 60

    def get_tracked_coins(self) -> List[str]:
        coins_raw = self.settings.get("TRACKED_COINS", "")
        return [coin.strip().lower() for coin in coins_raw.split(",") if coin.strip()]

    def get_api_url(self) -> str:
        return self.settings.get("COINGECKO_API_URL", "https://api.coingecko.com/api/v3")
