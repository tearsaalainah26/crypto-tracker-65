from datetime import datetime
from typing import Dict, List, Optional, Union


class CryptoAPIHandler:
    """Handles formatting and validation of cryptocurrency market data payloads."""

    def __init__(self, base_currency: str = "USD") -> None:
        """Initialize handler with default fiat base currency.

        Args:
            base_currency: Target fiat currency symbol (e.g., USD, EUR).
        """
        self.base_currency: str = base_currency.upper()

    def parse_ticker_response(
        self, raw_data: Dict[str, Union[str, float, int]]
    ) -> Dict[str, Union[str, float]]:
        """Extract standard price metrics from raw exchange API response.

        Args:
            raw_data: Dictionary containing raw payload from crypto exchange API.

        Returns:
            Normalized ticker dictionary with price and 24h change data.
        """
        symbol: str = str(raw_data.get("symbol", "UNKNOWN")).upper()
        price: float = float(raw_data.get("lastPrice", 0.0))
        change_24h: float = float(raw_data.get("priceChangePercent", 0.0))

        return {
            "symbol": symbol,
            "price": price,
            "currency": self.base_currency,
            "change_24h": change_24h,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def calculate_portfolio_value(
        self,
        holdings: Dict[str, float],
        prices: Dict[str, float],
    ) -> Dict[str, float]:
        """Calculate current total value and individual token values.

        Args:
            holdings: Map of crypto token symbols to token quantity.
            prices: Map of crypto token symbols to current unit prices.

        Returns:
            Dictionary containing total value and individual asset values.
        """
        total_value: float = 0.0
        breakdown: Dict[str, float] = {}

        for symbol, amount in holdings.items():
            unit_price: float = prices.get(symbol.upper(), 0.0)
            asset_val: float = amount * unit_price
            breakdown[symbol.upper()] = round(asset_val, 2)
            total_value += asset_val

        breakdown["total_value"] = round(total_value, 2)
        return breakdown
