import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = "crypto_tracker.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def setup_logger(name: str) -> logging.Logger:
    """Configures a rotating file logger for the tracker."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotating file handler configuration
        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        
        # Stream handler for console output
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger