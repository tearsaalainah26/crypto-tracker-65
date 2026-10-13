import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'crypto-tracker-65', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for the crypto-tracker application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate files: max 5MB, keep 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Also output to console for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger