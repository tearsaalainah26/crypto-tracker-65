import logging
from typing import Dict, Any, List, Optional
from decimal import Decimal, InvalidOperation

logger = logging.getLogger(__name__)

SUPPORTED_SYMBOLS = {"BTC-USD", "ETH-USD", "SOL-USD", "ADA-USD", "XRP-USD"}

class CryptoPayloadProcessor:
    """Processes incoming cryptocurrency raw tickers with strict input validation."""

    def __init__(self, supported_symbols: Optional[set] = None):
        self.supported_symbols = supported_symbols or SUPPORTED_SYMBOLS
        self.processed_count = 0

    def validate_payload(self, raw_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validates payload structure, data types, and value bounds."""
        if not isinstance(raw_data, dict):
            logger.warning("Rejected payload: Root element is not a dictionary.")
            return None

        symbol = raw_data.get("symbol")
        if not symbol or not isinstance(symbol, str) or symbol.upper() not in self.supported_symbols:
            logger.warning(f"Rejected payload: Invalid or unsupported symbol '{symbol}'.")
            return None

        try:
            price = Decimal(str(raw_data.get("price", "")))
            if price <= 0:
                logger.warning(f"Rejected payload for {symbol}: Price must be positive (got {price}).")
                return None
        except (InvalidOperation, TypeError):
            logger.warning(f"Rejected payload for {symbol}: Malformed price value.")
            return None

        try:
            volume = Decimal(str(raw_data.get("volume", "")))
            if volume < 0:
                logger.warning(f"Rejected payload for {symbol}: Volume cannot be negative (got {volume}).")
                return None
        except (InvalidOperation, TypeError):
            logger.warning(f"Rejected payload for {symbol}: Malformed volume value.")
            return None

        return {
            "symbol": symbol.upper(),
            "price": price,
            "volume": volume,
            "timestamp": raw_data.get("timestamp")
        }

    def process_incoming_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop that validates and transforms raw market data records."""
        valid_records = []
        for raw_item in batch:
            validated = self.validate_payload(raw_item)
            if validated:
                valid_records.append(validated)
                self.processed_count += 1
                logger.debug(f"Successfully processed ticker for {validated['symbol']}")

        return valid_records