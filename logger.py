import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a standardized logger instance for the crypto-tracker-65 application.

    Args:
        name (str): Name of the logger instance.
        level (int): Logging threshold level.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger

def log_trade_event(logger: logging.Logger, symbol: str, amount: float, price: float) -> None:
    """
    Logs a formatted trade execution event for auditing purposes.

    Args:
        logger (logging.Logger): The active logger instance.
        symbol (str): Cryptocurrency trading pair.
        amount (float): Quantity of assets traded.
        price (float): Execution price of the trade.
    """
    logger.info(f"Trade executed: {symbol} | Amount: {amount:.4f} | Price: ${price:.2f}")