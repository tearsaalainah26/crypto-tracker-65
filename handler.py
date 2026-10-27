import logging
from typing import Dict, Optional, Any

# Configure logging for data processing
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('crypto-tracker-65')

def normalize_crypto_data(raw_data: Dict[str, Any]) -> Optional[Dict[str, float]]:
    """
    Extracts price and volume from raw exchange API responses.
    Ensures numerical consistency for tracking.
    """
    try:
        ticker = raw_data.get('symbol', 'UNKNOWN')
        price = float(raw_data.get('price', 0.0))
        volume = float(raw_data.get('volume_24h', 0.0))
        
        if price <= 0:
            logger.warning(f"Invalid price received for {ticker}: {price}")
            return None
            
        return {
            'symbol': ticker.upper(),
            'price': price,
            'volume': volume,
            'timestamp': raw_data.get('ts')
        }
    except (ValueError, TypeError) as e:
        logger.error(f"Data parsing failure: {e}")
        return None

def calculate_percentage_change(current: float, previous: float) -> float:
    """
    Calculates relative change between two price points.
    """
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100