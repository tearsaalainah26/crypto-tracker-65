import logging
import sys
from logging.handlers import RotatingFileHandler

def get_logger(name: str) -> logging.Logger:
    """Initializes a standard logger for the crypto-tracker-65 application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler (max 5MB per file, keep 3 backups)
    file_handler = RotatingFileHandler(
        'crypto_tracker.log', 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def log_trade_event(logger: logging.Logger, symbol: str, action: str, price: float) -> None:
    """Logs specific crypto trading events with formatted data."""
    logger.info(f"Trade event: {action.upper()} {symbol} at ${price:,.2f}")

def log_error(logger: logging.Logger, error: Exception) -> None:
    """Logs exception details for debugging purposes."""
    logger.error(f"Application error encountered: {str(error)}", exc_info=True)