from typing import Dict, Any

class CryptoProcessor:
    """Processes raw cryptocurrency market data to extract insights and metrics."""

    def __init__(self, base_currency: str = "USD") -> None:
        """Initialize the processor with a default target currency.

        Args:
            base_currency: The currency symbol to format values against (e.g., 'USD', 'EUR').
        """
        self.base_currency: str = base_currency.upper()

    def calculate_price_change(self, initial_price: float, current_price: float) -> float:
        """Calculate the percentage change between an initial and a current price.

        Args:
            initial_price: The starting price of the asset.
            current_price: The current price of the asset.

        Returns:
            The percentage change as a float (e.g., 5.5 for a 5.5% increase).
        """
        if initial_price <= 0:
            raise ValueError("Initial price must be greater than zero.")
        
        return ((current_price - initial_price) / initial_price) * 100.0

    def is_highly_volatile(self, percentage_change: float, threshold: float = 5.0) -> bool:
        """Determine if a price change exceeds a specific volatility threshold.

        Args:
            percentage_change: The calculated percentage price movement.
            threshold: The volatility limit percentage.

        Returns:
            True if absolute change exceeds the threshold, False otherwise.
        """
        return abs(percentage_change) >= threshold

    def format_summary(self, symbol: str, current_price: float, price_change: float) -> Dict[str, Any]:
        """Format processed metric data into a standardized summary dictionary.

        Args:
            symbol: The ticker symbol (e.g., 'BTC').
            current_price: The latest market price.
            price_change: The pre-calculated percentage change.

        Returns:
            A dictionary containing formatted crypto tracking metrics.
        """
        return {
            "symbol": symbol.upper(),
            "price": f"{current_price:.2f} {self.base_currency}",
            "change_percent": f"{price_change:+.2f}%",
            "is_volatile": self.is_highly_volatile(price_change)
        }
