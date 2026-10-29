"""Crypto ticker and price feed data processor."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TickerData:
    symbol: str
    price: float
    volume_24h: float
    change_24h_pct: float


class CryptoDataProcessor:
    """Processes raw market updates and calculates price thresholds."""

    def __init__(self, price_alerts: Optional[Dict[str, float]] = None):
        self.alerts = price_alerts or {}

    def normalize_ticker(self, raw_payload: dict) -> Optional[TickerData]:
        """Converts raw WebSocket payload into a normalized TickerData object."""
        symbol = raw_payload.get("symbol") or raw_payload.get("pair")
        if not symbol or "last_price" not in raw_payload:
            return None

        try:
            return TickerData(
                symbol=symbol.upper(),
                price=float(raw_payload["last_price"]),
                volume_24h=float(raw_payload.get("volume", 0.0)),
                change_24h_pct=float(raw_payload.get("change_pct", 0.0)),
            )
        except (ValueError, TypeError):
            return None

    def check_alert_triggers(self, ticker: TickerData) -> List[str]:
        """Evaluates price alerts against current ticker values."""
        triggered = []
        target_price = self.alerts.get(ticker.symbol)

        if target_price and ticker.price >= target_price:
            triggered.append(
                f"ALERT: {ticker.symbol} reached target price of ${target_price:.2f} (Current: ${ticker.price:.2f})"
            )

        if abs(ticker.change_24h_pct) >= 10.0:
            direction = "surged" if ticker.change_24h_pct > 0 else "dropped"
            triggered.append(
                f"VOLATILITY: {ticker.symbol} {direction} by {ticker.change_24h_pct:.2f}% in 24h"
            )

        return triggered

    def process_batch(self, payload_list: List[dict]) -> Dict[str, TickerData]:
        """Cleans and aggregates a batch of raw exchange tickers."""
        processed = {}
        for payload in payload_list:
            ticker = self.normalize_ticker(payload)
            if ticker:
                processed[ticker.symbol] = ticker
        return processed
