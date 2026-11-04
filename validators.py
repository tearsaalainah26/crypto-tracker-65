from functools import lru_cache
import re

# Compiled regex patterns for performance optimization
SYMBOL_PATTERN = re.compile(r'^[A-Z]{2,10}$')

@lru_cache(maxsize=128)
def is_valid_symbol(symbol: str) -> bool:
    """Validates crypto ticker format with cached results."""
    if not isinstance(symbol, str):
        return False
    return bool(SYMBOL_PATTERN.match(symbol.strip().upper()))

def validate_batch(symbols: list[str]) -> list[str]:
    """Filters a list of symbols for valid formats."""
    return [s for s in symbols if is_valid_symbol(s)]

class DataValidator:
    """Core validation service for price feed updates."""
    
    @staticmethod
    def validate_price(price: float) -> bool:
        """Ensures price data is within non-negative bounds."""
        return isinstance(price, (int, float)) and price >= 0

    def process_payload(self, data: dict) -> dict:
        """Sanitizes incoming ticker payload dictionary."""
        return {
            k: v for k, v in data.items() 
            if is_valid_symbol(k) and self.validate_price(v)
        }