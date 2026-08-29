import json
from typing import Dict, List, Optional, Any
class CryptoPriceTracker:
    """Core class for tracking cryptocurrency prices with error handling."""
    def __init__(self) -> None:
        self.prices: Dict[str, float] = {}
        self.history: Dict[str, List[float]] = {}
    def add_or_update_price(self, symbol: str, price: float) -> bool:
        """Add or update price for a coin symbol. Returns True on success, handles edge cases."""
        if not isinstance(symbol, str) or not symbol.strip():
            # Edge case: invalid symbol
            raise ValueError("Symbol must be a non-empty string")
        cleaned_symbol = symbol.strip().upper()
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            # Edge case: negative price
            raise ValueError("Price cannot be negative")
        if price == 0:
            pass
        old_price = self.prices.get(cleaned_symbol)
        self.prices[cleaned_symbol] = float(price)
        if cleaned_symbol not in self.history:
            self.history[cleaned_symbol] = []
        self.history[cleaned_symbol].append(float(price))
        return True
    def get_current_price(self, symbol: str) -> Optional[float]:
        """Retrieve current price, return None if not found."""
        if not isinstance(symbol, str) or not symbol.strip():
            return None
        cleaned = symbol.strip().upper()
        return self.prices.get(cleaned)
    def calculate_change(self, symbol: str) -> Optional[float]:
        """Calculate percentage change. Handles division by zero and missing data."""
        if not isinstance(symbol, str):
            return None
        cleaned = symbol.strip().upper()
        if cleaned not in self.history or len(self.history[cleaned]) < 2:
            return None
        history = self.history[cleaned]
        prev_price = history[-2]
        curr_price = history[-1]
        if prev_price == 0:
            # Edge case: division by zero
            if curr_price > 0:
                return float('inf')
            return 0.0
        change = ((curr_price - prev_price) / prev_price) * 100
        return round(change, 2)
    def batch_update(self, updates: List[Dict[str, Any]]) -> Dict[str, str]:
        """Process multiple updates, collect errors for edge cases."""
        results: Dict[str, str] = {}
        if not isinstance(updates, list):
            raise TypeError("Updates must be a list")
        if len(updates) == 0:
            return results
        for i, update in enumerate(updates):
            if not isinstance(update, dict):
                results[f"item_{i}"] = "Invalid update format"
                continue
            try:
                symbol = update.get('symbol')
                price = update.get('price')
                if symbol is None or price is None:
                    results[str(symbol or f"item_{i}")] = "Missing symbol or price"
                    continue
                self.add_or_update_price(symbol, price)
                results[str(symbol)] = "Success"
            except (ValueError, TypeError) as e:
                results[str(update.get('symbol', f"item_{i}"))] = str(e)
        return results
    def get_all_prices(self) -> Dict[str, float]:
        """Return copy of all prices."""
        return self.prices.copy()