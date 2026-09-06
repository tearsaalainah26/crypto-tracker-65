import functools
from typing import Dict, List

# Cache for crypto price calculations to reduce CPU overhead
@functools.lru_cache(maxsize=128)
def calculate_portfolio_value(prices: Dict[str, float], holdings: Dict[str, float]) -> float:
    """Calculates total value using cached lookups for performance."""
    total = 0.0
    for coin, amount in holdings.items():
        price = prices.get(coin, 0.0)
        total += price * amount
    return total

class DataProcessor:
    """High-performance data processing for crypto-tracker-65."""
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def process_market_data(self, data: List[Dict]) -> List[Dict]:
        """Efficient batch processing of raw market ticks."""
        if not data:
            return []
        
        # Use list comprehension for faster iteration
        return [
            {
                'symbol': item.get('s'),
                'price': float(item.get('p', 0)),
                'volume': float(item.get('v', 0))
            }
            for item in data
        ]

    def get_summary(self, prices: Dict, holdings: Dict) -> Dict:
        """Provides optimized calculation interface."""
        return {
            'total_value': calculate_portfolio_value(tuple(sorted(prices.items())), tuple(sorted(holdings.items()))),
            'asset_count': len(holdings)
        }