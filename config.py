import os
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass(frozen=True)
class TrackerConfig:
    api_key: str
    base_url: str
    tracked_coins: List[str] = field(default_factory=lambda: ["bitcoin", "ethereum", "solana"])
    update_interval: int = 60  # in seconds
    fiat_currency: str = "usd"

    @classmethod
    def from_env(cls) -> "TrackerConfig":
        """Loads tracker configuration from environment variables with safe fallbacks."""
        api_key = os.getenv("CRYPTO_TRACKER_API_KEY", "demo_key_12345")
        base_url = os.getenv("CRYPTO_TRACKER_BASE_URL", "https://api.coingecko.com/v3")
        
        coins_raw = os.getenv("CRYPTO_TRACKER_COINS")
        if coins_raw:
            coins = [coin.strip().lower() for coin in coins_raw.split(",") if coin.strip()]
        else:
            coins = ["bitcoin", "ethereum", "solana"]

        try:
            interval = int(os.getenv("CRYPTO_TRACKER_INTERVAL", "60"))
        except ValueError:
            interval = 60

        fiat = os.getenv("CRYPTO_TRACKER_FIAT", "usd").strip().lower()

        return cls(
            api_key=api_key,
            base_url=base_url,
            tracked_coins=coins,
            update_interval=interval,
            fiat_currency=fiat
        )

    def to_dict(self) -> Dict[str, Any]:
        """Returns configuration settings with a masked API key for safe logging."""
        masked_key = f"{self.api_key[:4]}...{self.api_key[-4:]}" if len(self.api_key) > 8 else "***"
        return {
            "base_url": self.base_url,
            "tracked_coins": self.tracked_coins,
            "update_interval": self.update_interval,
            "fiat_currency": self.fiat_currency,
            "api_key_masked": masked_key
        }