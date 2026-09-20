"""Data processing utilities for cryptocurrency ticker payloads."""

from typing import Any, Dict, List, Optional


class CryptoDataProcessor:
    """Processes, normalizes, and filters raw cryptocurrency market data."""

    def __init__(self, target_currency: str = "USD") -> None:
        self.target_currency = target_currency.upper()

    def normalize_ticker(self, raw_ticker: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize market ticker dictionary structure."""
        symbol = str(raw_ticker.get("symbol", "")).upper()
        price = float(raw_ticker.get("price", 0.0))
        volume = float(raw_ticker.get("volume_24h", raw_ticker.get("volume", 0.0)))
        change_24h = float(raw_ticker.get("change_24h", 0.0))

        return {
            "symbol": symbol,
            "price": round(price, 8 if price < 1.0 else 2),
            "volume_24h": round(volume, 2),
            "change_24h_percent": round(change_24h, 2),
            "quote_currency": self.target_currency,
        }

    def filter_high_volume(
        self, tickers: List[Dict[str, Any]], min_volume: float = 10000.0
    ) -> List[Dict[str, Any]]:
        """Filter out tickers below a specified 24-hour trading volume."""
        cleaned_tickers = [self.normalize_ticker(t) for t in tickers]
        return [t for t in cleaned_tickers if t["volume_24h"] >= min_volume]

    def calculate_portfolio_value(
        self, holdings: Dict[str, float], tickers: List[Dict[str, Any]]
    ) -> Dict[str, float]:
        """Calculate aggregate portfolio value based on latest ticker prices."""
        price_map = {t["symbol"]: t["price"] for t in tickers if "symbol" in t}
        total_value = 0.0
        details = {}

        for asset, amount in holdings.items():
            asset_symbol = asset.upper()
            unit_price = price_map.get(asset_symbol, 0.0)
            asset_value = round(amount * unit_price, 2)
            details[asset_symbol] = asset_value
            total_value += asset_value

        details["TOTAL"] = round(total_value, 2)
        return details