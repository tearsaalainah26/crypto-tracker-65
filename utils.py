from typing import Dict, Tuple


def calculate_price_metrics(
    current_price: float, previous_price: float
) -> Dict[str, float]:
    """Calculate absolute and percentage change between two price points."""
    if previous_price <= 0:
        raise ValueError("Previous price must be greater than zero")

    absolute_change = current_price - previous_price
    percentage_change = (absolute_change / previous_price) * 100

    return {
        "current_price": round(current_price, 8),
        "previous_price": round(previous_price, 8),
        "absolute_change": round(absolute_change, 8),
        "percentage_change": round(percentage_change, 4),
    }


def parse_symbol_pair(symbol: str) -> Tuple[str, str]:
    """Parse unified symbol string into base and quote currencies."""
    clean_symbol = symbol.upper().strip()

    for delimiter in ["/", "-", "_"]:
        if delimiter in clean_symbol:
            parts = clean_symbol.split(delimiter)
            if len(parts) == 2 and parts[0] and parts[1]:
                return parts[0], parts[1]

    common_quotes = ["USDT", "USDC", "BUSD", "USD", "BTC", "ETH", "EUR"]
    for quote in common_quotes:
        if clean_symbol.endswith(quote) and len(clean_symbol) > len(quote):
            base = clean_symbol[: -len(quote)]
            return base, quote

    raise ValueError(f"Unable to parse trading pair: {symbol}")


def format_crypto_display(
    amount: float, symbol: str, is_quote: bool = False
) -> str:
    """Format crypto amounts with appropriate decimal precision based on value."""
    if is_quote or amount >= 1000:
        return f"{amount:,.2f} {symbol}"
    if amount >= 1:
        return f"{amount:,.4f} {symbol}"
    return f"{amount:,.8f} {symbol}"
