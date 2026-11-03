import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class BatchProcessor:
    """Processes incoming cryptocurrency tracking requests with strict input validation."""

    def __init__(self, default_currency: str = "USD") -> None:
        self.default_currency = default_currency
        self.processed_count = 0
        self.error_count = 0

    def validate_payload(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validate raw input payload attributes before execution."""
        if not isinstance(item, dict):
            logger.warning("Invalid item format, expected dict: %s", type(item).__name__)
            return None

        symbol = item.get("symbol")
        if not symbol or not isinstance(symbol, str):
            logger.warning("Missing or non-string 'symbol' field: %s", symbol)
            return None

        cleaned_symbol = symbol.strip().upper()
        if not (2 <= len(cleaned_symbol) <= 10) or not cleaned_symbol.isalnum():
            logger.warning("Malformed ticker symbol format: %s", cleaned_symbol)
            return None

        raw_amount = item.get("amount", 0.0)
        try:
            amount = float(raw_amount)
            if amount < 0:
                logger.warning("Negative transaction amount for %s: %f", cleaned_symbol, amount)
                return None
        except (ValueError, TypeError):
            logger.warning("Invalid numerical value for amount: %s", raw_amount)
            return None

        return {
            "symbol": cleaned_symbol,
            "amount": amount,
            "currency": str(item.get("currency", self.default_currency)).upper().strip()
        }

    def process_batch(self, input_batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Iterate through a batch of payloads, validating each item in the main loop."""
        validated_results = []
        for raw_item in input_batch:
            validated_data = self.validate_payload(raw_item)
            if not validated_data:
                self.error_count += 1
                continue

            validated_results.append(validated_data)
            self.processed_count += 1

        logger.info("Batch complete: %d valid, %d rejected", len(validated_results), self.error_count)
        return validated_results
