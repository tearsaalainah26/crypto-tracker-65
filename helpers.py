from typing import Union


def format_crypto_price(price: Union[int, float]) -> str:
    """
    Formats a crypto price to an appropriate decimal precision.
    Displays up to 8 decimals for micro-cap assets, and standard 2-4 decimals for others.
    """
    price_float = float(price)
    if price_float <= 0:
        return "$0.00"

    if price_float < 0.0001:
        return f"${price_float:.8f}"
    elif price_float < 1.0:
        return f"${price_float:.6f}"
    elif price_float < 100.0:
        return f"${price_float:.4f}"
    else:
        return f"${price_float:,.2f}"


def calculate_price_change(old_price: float, new_price: float) -> float:
    """
    Safely calculates the percentage change between two prices.
    Returns 0.0 if the old price is invalid or zero.
    """
    if not old_price or old_price <= 0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100.0


def format_fiat_volume(volume: Union[int, float]) -> str:
    """
    Converts large raw market cap or volume numbers to human-readable formats (K, M, B, T).
    """
    val = float(volume)
    if val < 1000:
        return f"${val:.2f}"

    for unit in ["", "K", "M", "B", "T"]:
        if abs(val) < 1000.0:
            return f"${val:.2f}{unit}"
        val /= 1000.0
    return f"${val:.2f}P"
