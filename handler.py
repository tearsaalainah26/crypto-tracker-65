from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class CryptoHandler:
    """Handles market data processing for crypto-tracker-65."""

    def __init__(self, api_key: str, base_currency: str = "USD"):
        """Initialize the handler with authentication and settings."""
        self.api_key = api_key
        self.base_currency = base_currency

    def process_ticker_update(self, data: Dict[str, Any]) -> Optional[float]:
        """Extract price from ticker update payload."""
        try:
            price = data.get("price")
            if not isinstance(price, (int, float)):
                return None
            return float(price)
        except (ValueError, TypeError) as e:
            logger.error(f"Data parsing error: {e}")
            return None

    def format_portfolio(self, holdings: List[Dict[str, Any]]) -> Dict[str, float]:
        """Aggregate current holdings into a summary dictionary."""
        summary: Dict[str, float] = {}
        for item in holdings:
            symbol = str(item.get("symbol", "UNKNOWN"))
            amount = float(item.get("amount", 0.0))
            summary[symbol] = summary.get(symbol, 0.0) + amount
        return summary