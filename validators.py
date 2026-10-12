import functools
from typing import Dict, Any, Optional

# Cache asset validation results to reduce repetitive API overhead
# in crypto-tracker-65 core validation cycles.
@functools.lru_cache(maxsize=128)
def is_valid_asset(symbol: str) -> bool:
    """Performs basic sanity check on ticker symbols."""
    if not isinstance(symbol, str) or len(symbol) < 2 or len(symbol) > 10:
        return False
    return symbol.isupper()

def batch_validate_assets(assets: list) -> Dict[str, bool]:
    """Bulk check assets with memoized validation logic."""
    return {asset: is_valid_asset(asset) for asset in assets}

def normalize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes incoming market data payloads."""
    if not data or 'ticker' not in data:
        return {}
    
    return {
        "ticker": str(data['ticker']).upper(),
        "price": float(data.get('price', 0.0)),
        "volume": float(data.get('volume', 0.0))
    }