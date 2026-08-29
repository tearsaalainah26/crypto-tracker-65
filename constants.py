"""
Constants for crypto-tracker-65.

Defines constants with type annotations and includes docstrings
for helper functions to access them.
"""

from typing import Dict, List, Final, Optional

# API configuration constants
API_BASE_URL: Final[str] = "https://api.coingecko.com/api/v3"
API_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported assets
SUPPORTED_CRYPTOS: Final[Dict[str, str]] = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "solana": "Solana",
    "cardano": "Cardano",
    "polkadot": "Polkadot",
}

FIAT_CURRENCIES: Final[List[str]] = ["usd", "eur", "gbp", "jpy"]

# Settings
DEFAULT_INTERVAL: Final[int] = 60
THRESHOLD: Final[float] = 0.05
MAX_ASSETS: Final[int] = 5

EXCHANGE_APIS: Final[Dict[str, str]] = {
    "coingecko": API_BASE_URL,
    "binance": "https://api.binance.com/api/v3",
}

def get_supported_cryptos() -> List[str]:
    """Return list of supported crypto IDs.

    Returns:
        List of cryptocurrency IDs.
    """
    return list(SUPPORTED_CRYPTOS.keys())

def get_crypto_full_name(crypto_id: str) -> Optional[str]:
    """Get full name for crypto ID.

    Args:
        crypto_id: ID of the crypto.

    Returns:
        Full name or None.
    """
    return SUPPORTED_CRYPTOS.get(crypto_id)

def get_api_for_exchange(exchange: str) -> Optional[str]:
    """Retrieve API URL for given exchange.

    Args:
        exchange: Exchange name.

    Returns:
        API base URL or None.
    """
    return EXCHANGE_APIS.get(exchange)
