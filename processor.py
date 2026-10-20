from typing import List, Dict, Any
import datetime


class MarketDataProcessor:
    """Processes raw cryptocurrency market data for analysis and tracking."""

    def __init__(self, base_currency: str = "USD") -> None:
        self.base_currency: str = base_currency.upper()

    def calculate_vwap(self, trades: List[Dict[str, float]]) -> float:
        """Calculate the Volume-Weighted Average Price (VWAP) from trade ticks.

        Args:
            trades: A list of dicts containing 'price' and 'volume' keys.

        Returns:
            The volume-weighted average price as a float.
        """
        if not trades:
            return 0.0

        total_volume: float = sum(trade.get("volume", 0.0) for trade in trades)
        if total_volume == 0.0:
            return 0.0

        total_price_volume: float = sum(
            trade.get("price", 0.0) * trade.get("volume", 0.0) for trade in trades
        )
        return round(total_price_volume / total_volume, 4)

    def format_ticker_summary(
        self, symbol: str, current_price: float, price_24h_ago: float, volume_24h: float
    ) -> Dict[str, Any]:
        """Format a summary dict for display in the crypto tracker interface.

        Args:
            symbol: Ticker symbol (e.g., 'BTC').
            current_price: Current market price.
            price_24h_ago: Price 24 hours prior.
            volume_24h: Total volume in 24 hours.

        Returns:
            Formatted market summary dictionary.
        """
        price_change: float = current_price - price_24h_ago
        percent_change: float = (
            (price_change / price_24h_ago) * 100 if price_24h_ago > 0 else 0.0
        )

        return {
            "symbol": f"{symbol.upper()}/{self.base_currency}",
            "price": round(current_price, 2),
            "change_24h": round(price_change, 2),
            "percent_change_24h": round(percent_change, 2),
            "volume_24h": round(volume_24h, 2),
            "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
