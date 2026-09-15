import json
import logging
from typing import Dict, Any

logger = logging.getLogger("crypto_tracker.handler")

class MarketDataParseError(Exception):
    """Custom exception for market data parsing failures."""
    pass

class CryptoAPIHandler:
    """Handles parsing and validation of cryptocurrency API payloads."""

    @staticmethod
    def parse_ticker_data(raw_response: str) -> Dict[str, Any]:
        """
        Parses and validates raw ticker JSON response from a crypto API.
        
        Handles edge cases such as invalid JSON, missing keys, type mismatches,
        and unexpected price anomalies like negative or zero values.
        """
        if not raw_response or not raw_response.strip():
            raise MarketDataParseError("Received empty payload from API")

        try:
            data = json.loads(raw_response)
        except json.JSONDecodeError as err:
            raise MarketDataParseError(f"Malformed JSON response: {err}")

        if not isinstance(data, dict):
            raise MarketDataParseError("Invalid API response format: expected a dictionary")

        required_keys = ["symbol", "price", "volume_24h"]
        for key in required_keys:
            if key not in data:
                raise MarketDataParseError(f"Missing required key in response: {key}")

        symbol = str(data["symbol"]).upper().strip()
        if not symbol:
            raise MarketDataParseError("Symbol field cannot be empty")

        try:
            price = float(data["price"])
            volume = float(data["volume_24h"])
        except (ValueError, TypeError) as err:
            raise MarketDataParseError(f"Numeric validation error for price or volume: {err}")

        if price <= 0:
            raise MarketDataParseError(f"Invalid non-positive price encountered: {price}")
        if volume < 0:
            raise MarketDataParseError(f"Invalid negative volume encountered: {volume}")

        return {
            "symbol": symbol,
            "price": price,
            "volume_24h": volume,
            "change_24h": float(data.get("change_24h", 0.0))
        }