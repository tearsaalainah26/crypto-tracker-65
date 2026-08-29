import datetime
from typing import List, Dict, Any, Optional

def process_raw_ticker_data(raw_data: List[Dict[str, Any]]) -> Dict[str, float]:
    """Convert raw ticker data to symbol-price mapping."""
    processed = {}
    for item in raw_data:
        symbol = item.get('symbol', '').upper()
        price = item.get('price', 0)
        if symbol and isinstance(price, (int, float)):
            processed[symbol] = float(price)
    return processed

def calculate_portfolio_value(holdings: Dict[str, float], current_prices: Dict[str, float]) -> float:
    """Calculate current total value of holdings."""
    total = 0.0
    for symbol, amount in holdings.items():
        price = current_prices.get(symbol.upper(), 0.0)
        total += amount * price
    return total

def get_price_changes(old_prices: Dict[str, float], new_prices: Dict[str, float]) -> Dict[str, float]:
    """Compute percentage price changes."""
    changes = {}
    for symbol, old_price in old_prices.items():
        new_price = new_prices.get(symbol, 0.0)
        if old_price > 0:
            change = ((new_price - old_price) / old_price) * 100
            changes[symbol] = round(change, 2)
    return changes

def filter_high_volume(data: List[Dict[str, Any]], min_volume: float = 1000000) -> List[Dict[str, Any]]:
    """Filter cryptos with high trading volume."""
    filtered = []
    for item in data:
        volume = item.get('volume', 0)
        if isinstance(volume, (int, float)) and volume >= min_volume:
            filtered.append(item)
    return filtered

def format_timestamp(ts: Optional[int] = None) -> str:
    """Format current or given timestamp."""
    if ts is None:
        ts = int(datetime.datetime.now().timestamp())
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def compute_moving_average(prices: List[float], window: int = 5) -> float:
    """Calculate simple moving average."""
    if len(prices) < window:
        return sum(prices) / len(prices) if prices else 0.0
    recent = prices[-window:]
    return sum(recent) / window