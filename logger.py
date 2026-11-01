import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = "crypto_tracker.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def setup_logger(name: str) -> logging.Logger:
    """Configures a rotating file logger for the application."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # File handler with rotation
    file_path = os.path.join(LOG_DIR, LOG_FILE)
    handler = RotatingFileHandler(
        file_path, 
        maxBytes=MAX_BYTES, 
        backupCount=BACKUP_COUNT
    )
    handler.setFormatter(formatter)

    # Console handler for visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console)

    return logger