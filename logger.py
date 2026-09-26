import logging
import os
import sys
from typing import Any, Dict, Optional


class CryptoLogger:
    """Custom logger wrapper for crypto tracking operations with fallback handling."""

    def __init__(self, name: str = "crypto_tracker", log_file: Optional[str] = "crypto_tracker.log", level: str = "INFO"):
        self.logger = logging.getLogger(name)
        if self.logger.handlers:
            return

        numeric_level = getattr(logging, str(level).upper(), None)
        if not isinstance(numeric_level, int):
            numeric_level = logging.INFO

        self.logger.setLevel(numeric_level)
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if log_file:
            try:
                log_dir = os.path.dirname(log_file)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir, exist_ok=True)

                file_handler = logging.FileHandler(log_file, encoding="utf-8")
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
            except (OSError, PermissionError) as err:
                self.logger.warning(f"Failed to setup log file '{log_file}': {err}. Defaulting to stdout.")

    def log_trade(self, symbol: str, price: float, amount: float, extra: Optional[Dict[str, Any]] = None) -> None:
        """Safely format and log trade events handling missing or corrupted metadata."""
        try:
            safe_symbol = str(symbol).upper() if symbol else "UNKNOWN"
            safe_price = float(price) if price is not None else 0.0
            safe_amount = float(amount) if amount is not None else 0.0
            msg = f"TRADE | Symbol: {safe_symbol} | Price: ${safe_price:,.4f} | Amount: {safe_amount:,}"
            if extra and isinstance(extra, dict):
                msg += f" | Metadata: {extra}"
            self.logger.info(msg)
        except (ValueError, TypeError) as err:
            self.logger.error(f"Malformed trade log entry for symbol '{symbol}': {err}")


def get_logger(name: str = "crypto_tracker") -> logging.Logger:
    """Retrieve configured logger instance."""
    return CryptoLogger(name=name).logger
