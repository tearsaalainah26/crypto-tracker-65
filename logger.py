import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = "crypto_tracker.log", level=logging.INFO):
    """
    Configures a rotating file logger for crypto-tracker-65 components.
    Maintains up to 5 files of 5MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # File rotation setup
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=5
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Console output for visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Default logger instance
logger = setup_logger("crypto_tracker_65")