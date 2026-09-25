from typing import Dict, Any, List, Optional
import requests

def format_currency(amount: float, symbol: str = 'USD') -> str:
    """Formats a float amount into a currency string."""
    return f"{amount:,.2f} {symbol}"

def fetch_ticker_data(api_url: str, symbols: List[str]) -> Dict[str, Any]:
    """Fetches price data for a list of crypto symbols."""
    params = {"ids": ",".join(symbols), "vs_currencies": "usd"}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()

def calculate_portfolio_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Calculates total value of portfolio based on market prices."""
    total = 0.0
    for coin, quantity in holdings.items():
        price = prices.get(coin, {}).get('usd', 0.0)
        total += quantity * price
    return total

def validate_response_structure(data: Dict[str, Any], keys: List[str]) -> bool:
    """Ensures API response contains required keys."""
    return all(key in data for key in keys)