import logging
from typing import Dict, List, Optional

# Configure logging for crypto-tracker-65
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('crypto-tracker-65')

class CryptoTracker:
    def __init__(self, assets: List[str]):
        self.assets = assets
        self.prices: Dict[str, float] = {}

    def update_prices(self, provider_data: Dict[str, float]) -> None:
        """Synchronizes tracker state with new price data."""
        for asset in self.assets:
            price = provider_data.get(asset)
            if price is not None:
                self.prices[asset] = price
        logger.info(f"Updated {len(self.prices)} assets")

    def get_summary(self) -> str:
        """Formats asset prices for notification."""
        return ", ".join([f"{k}: ${v:.2f}" for k, v in self.prices.items()])

    def validate_input(self, data: Dict) -> bool:
        """Ensures incoming price payload contains required fields."""
        return all(asset in data for asset in self.assets)

def initialize_tracker(assets: List[str]) -> CryptoTracker:
    """Factory method for core tracker component."""
    logger.info("Initializing core crypto tracker")
    return CryptoTracker(assets=assets)