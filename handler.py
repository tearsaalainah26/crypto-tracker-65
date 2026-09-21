import logging
from typing import Dict, Any
from core import CryptoFetcher

logger = logging.getLogger(__name__)

class CryptoHandler:
    """Handles incoming crypto requests and orchestrates data fetching."""

    def __init__(self, fetcher: CryptoFetcher):
        self.fetcher = fetcher

    def process_request(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validates request and retrieves latest market data."""
        symbol = request_data.get("symbol")
        
        if not symbol:
            logger.error("Missing symbol in request data")
            return {"status": "error", "message": "symbol required"}

        try:
            data = self.fetcher.get_price(symbol)
            return {
                "status": "success",
                "symbol": symbol,
                "price": data.get("price"),
                "timestamp": data.get("ts")
            }
        except Exception as e:
            logger.exception(f"Failed to process symbol {symbol}")
            return {"status": "error", "message": str(e)}

    def batch_process(self, symbols: list) -> list:
        """Handles multiple symbol queries efficiently."""
        results = []
        for symbol in symbols:
            results.append(self.process_request({"symbol": symbol}))
        return results