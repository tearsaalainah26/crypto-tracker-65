import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='crypto-tracker-65', log_file='tracker.log'):
    """Configures a rotating file logger for system tracking."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate files at 5MB, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger