from typing import List, Dict, Any, Optional

class CryptoProcessor:
    """Processes cryptocurrency market data for analysis and filtering."""

    def __init__(self, raw_data: List[Dict[str, Any]]) -> None:
        """Initialize with raw data.

        Args:
            raw_data: List of crypto dicts with 'symbol', 'price', 'volume'.
        """
        self.data: List[Dict[str, Any]] = raw_data

    def filter_by_price(self, min_price: float, max_price: Optional[float] = None) -> List[Dict[str, Any]]:
        """Return data filtered to price range.

        Args:
            min_price: Lower bound for price.
            max_price: Upper bound, optional.
        Returns:
            Filtered list.
        """
        result = [d for d in self.data if d.get("price", 0) >= min_price]
        if max_price is not None:
            result = [d for d in result if d.get("price", 0) <= max_price]
        return result

    def calculate_average_price(self) -> float:
        """Calculate mean price of all items.

        Returns:
            Average price.
        """
        prices = [d.get("price", 0) for d in self.data]
        return sum(prices) / len(prices) if prices else 0.0

    def get_top_by_volume(self, n: int = 5) -> List[Dict[str, Any]]:
        """Get top n entries sorted by volume descending.

        Args:
            n: Number to return.
        Returns:
            Top n items.
        """
        return sorted(self.data, key=lambda x: x.get("volume", 0), reverse=True)[:n]

    def get_summary(self) -> Dict[str, Any]:
        """Create summary dict with stats.

        Returns:
            Dict containing average, count and top symbols.
        """
        avg = self.calculate_average_price()
        top = self.get_top_by_volume(3)
        symbols = [item.get("symbol", "") for item in top]
        return {"average_price": avg, "count": len(self.data), "top_symbols": symbols}

def process_crypto_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process data using CryptoProcessor and return summary.

    Args:
        data: Input list of crypto data.
    Returns:
        Summary dictionary.
    """
    processor = CryptoProcessor(data)
    return processor.get_summary()

if __name__ == "__main__":
    sample_data: List[Dict[str, Any]] = [
        {"symbol": "BTC", "price": 65000, "volume": 3e10},
        {"symbol": "ETH", "price": 2500, "volume": 1.5e10},
        {"symbol": "ADA", "price": 0.35, "volume": 5e8},
    ]
    summary = process_crypto_data(sample_data)
    print(summary)
