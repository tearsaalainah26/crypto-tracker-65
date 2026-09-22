import logging
import sys
from typing import Any

# crypto-tracker-65 logging utility

def get_logger(name: str) -> logging.Logger:
    """Configures a robust logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

def safe_log_error(logger: logging.Logger, error: Exception, context: str = "") -> None:
    """Standardized error handling for crypto API edge cases."""
    try:
        error_type = type(error).__name__
        error_msg = str(error) if str(error) else "Unknown error occurred"
        
        # Filter for specific critical error structures
        if isinstance(error, (ConnectionError, TimeoutError)):
            logger.error(f"Network failure in {context}: {error_type} - {error_msg}")
        elif isinstance(error, ValueError):
            logger.warning(f"Data validation failure in {context}: {error_msg}")
        else:
            logger.critical(f"Unexpected system exception in {context}: {error_type} - {error_msg}")
            
    except Exception as fallback_error:
        # Failsafe for logger internal failures
        print(f"Critical logging failure: {fallback_error}")

def log_trade_event(logger: logging.Logger, trade_data: dict[str, Any]) -> None:
    """Safe logging for trade events with key presence check."""
    required_keys = ['symbol', 'amount', 'price']
    if all(k in trade_data for k in required_keys):
        logger.info(f"Trade executed: {trade_data['symbol']} | {trade_data['amount']} @ {trade_data['price']}")
    else:
        logger.error("Incomplete trade data provided for logging")