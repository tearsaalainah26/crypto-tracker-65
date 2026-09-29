import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, currency_pair: str):
        self.currency_pair = currency_pair

    def sanitize_ticker_data(self, raw_data: List[Dict]) -> List[Dict]:
        """Removes incomplete records and normalizes field types."""
        cleaned = []
        for entry in raw_data:
            try:
                price = float(entry.get('price', 0))
                volume = float(entry.get('volume', 0))
                if price > 0:
                    cleaned.append({
                        'pair': self.currency_pair,
                        'price': price,
                        'volume': volume,
                        'timestamp': entry.get('ts')
                    })
            except (ValueError, TypeError) as e:
                logger.warning(f"skipping malformed record: {e}")
        return cleaned

    def calculate_moving_average(self, data: List[Dict], period: int = 24) -> Optional[float]:
        """Computes simple moving average for the price field."""
        if not data or len(data) < period:
            return None
        
        prices = [d['price'] for d in data[-period:]]
        return sum(prices) / len(prices)

    def process_batch(self, raw_data: List[Dict]) -> Dict:
        """Orchestrates normalization and analytical metrics."""
        clean_data = self.sanitize_ticker_data(raw_data)
        avg_price = self.calculate_moving_average(clean_data)
        
        return {
            'count': len(clean_data),
            'avg_price': avg_price,
            'pair': self.currency_pair
        }