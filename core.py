from typing import Dict, List, Optional

class CryptoTracker:
    """Manages tracking of cryptocurrency assets and price updates."""

    def __init__(self, symbols: List[str]) -> None:
        self.symbols: List[str] = symbols
        self.prices: Dict[str, float] = {}

    def update_price(self, symbol: str, price: float) -> None:
        """Updates internal price map for a specific ticker."""
        if symbol in self.symbols:
            self.prices[symbol] = price

    def get_portfolio_value(self, holdings: Dict[str, float]) -> float:
        """Calculates total value based on current price data."""
        total: float = 0.0
        for symbol, amount in holdings.items():
            price: Optional[float] = self.prices.get(symbol)
            if price is not None:
                total += price * amount
        return total

    def fetch_all_symbols(self) -> List[str]:
        """Returns the list of monitored cryptocurrency symbols."""
        return self.symbols

def format_currency(value: float, currency_code: str = "USD") -> str:
    """Converts float to standardized currency string format."""
    return f"{currency_code} {value:,.2f}"