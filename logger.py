import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'crypto-tracker-65', log_file: str = 'crypto.log') -> logging.Logger:
    """
    Configures a rotating file logger for the crypto-tracker application.
    Logs up to 5MB per file with a backup of 3 files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # 5MB per file, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instantiate standard application logger
crypto_logger = setup_logger()