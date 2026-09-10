import logging
import requests
from typing import Optional, Any

logger = logging.getLogger(__name__)

def fetch_price_data(url: str, timeout: int = 10) -> Optional[dict]:
    """Fetches crypto price data with defensive error handling."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        logger.error(f"Request to {url} timed out")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        logger.error(f"Failed to connect to {url}")
    except ValueError:
        logger.error(f"Failed to decode JSON response from {url}")
    except Exception as e:
        logger.error(f"Unexpected error during fetch: {e}")
    return None

def validate_ticker(ticker: Any) -> str:
    """Ensures ticker format is valid string."""
    if not isinstance(ticker, str) or not ticker.isalnum():
        raise ValueError(f"Invalid ticker format: {ticker}")
    return ticker.upper()