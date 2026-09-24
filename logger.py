import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'crypto-tracker-65', log_file: str = 'app.log'):
    """Configures a rotating file logger for tracking crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Rotation settings: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to console for development visibility
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger