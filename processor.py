from typing import Dict, List, Any, Optional
from datetime import datetime, timezone

class CryptoProcessor:
    """Processes and normalizes raw cryptocurrency market data."""

    def __init__(self, base_currency: str = "USD") -> None:
        self.base_currency = base_currency.upper()

    def clean_ticker_data(self, raw_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extracts and cleans essential ticker fields from raw API payload."""
        if not raw_data or "symbol" not in raw_data:
            return None

        price = float(raw_data.get("price", 0.0))
        volume = float(raw_data.get("volume", 0.0))
        change_24h = float(raw_data.get("change_24h", 0.0))

        return {
            "symbol": str(raw_data["symbol"]).upper(),
            "price": round(price, 4),
            "volume_24h": round(volume, 2),
            "change_24h_pct": round(change_24h, 2),
            "base_currency": self.base_currency,
            "processed_at": datetime.now(timezone.utc).isoformat(),
        }

    def batch_process_tickers(self, tickers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filters invalid records and processes a list of raw ticker payloads."""
        processed = []
        for item in tickers:
            cleaned = self.clean_ticker_data(item)
            if cleaned and cleaned["price"] > 0:
                processed.append(cleaned)
        return processed

    def calculate_portfolio_value(self, holdings: Dict[str, float], prices: Dict[str, float]) -> Dict[str, Any]:
        """Calculates total portfolio valuation from cleaned price mapping."""
        total_val = 0.0
        breakdown = {}

        for symbol, amount in holdings.items():
            sym_upper = symbol.upper()
            unit_price = prices.get(sym_upper, 0.0)
            asset_value = round(amount * unit_price, 2)
            breakdown[sym_upper] = asset_value
            total_val += asset_value

        return {
            "total_value": round(total_val, 2),
            "currency": self.base_currency,
            "breakdown": breakdown,
        }