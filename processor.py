import time
from typing import Dict, Any, List, Tuple, Optional

class CryptoProcessor:
    ALLOWED_SYMBOLS = {"BTC", "ETH", "SOL", "ADA", "DOT"}

    def __init__(self):
        self.processed_ticks: List[Dict[str, Any]] = []

    def validate_input(self, tick: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """Validate cryptocurrency tick data format and values."""
        if not isinstance(tick, dict):
            return False, "payload must be a dictionary"

        symbol = tick.get("symbol")
        if not isinstance(symbol, str) or symbol.upper() not in self.ALLOWED_SYMBOLS:
            return False, f"unsupported or invalid symbol: {symbol}"

        price = tick.get("price")
        if not isinstance(price, (int, float)) or price <= 0:
            return False, f"price must be a positive number, got: {price}"

        volume = tick.get("volume")
        if not isinstance(volume, (int, float)) or volume < 0:
            return False, f"volume must be non-negative, got: {volume}"

        timestamp = tick.get("timestamp")
        current_time = time.time()
        if not isinstance(timestamp, (int, float)) or timestamp > current_time + 60:
            return False, f"invalid or future timestamp: {timestamp}"

        return True, None

    def process_stream(self, data_stream: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop with input validation."""
        valid_entries = []
        for item in data_stream:
            is_valid, error = self.validate_input(item)
            if not is_valid:
                print(f"[VALIDATION_FAILED] {error}")
                continue

            clean_record = {
                "symbol": item["symbol"].upper(),
                "price": float(item["price"]),
                "volume": float(item["volume"]),
                "timestamp": float(item["timestamp"]),
                "processed_at": time.time()
            }
            valid_entries.append(clean_record)

        self.processed_ticks.extend(valid_entries)
        return valid_entries