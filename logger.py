import os
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "crypto_tracker.log"
MAX_LOG_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB per log file
BACKUP_COUNT = 5  # Keep 5 historical log files


def setup_logger(
    name: str = "crypto_tracker",
    log_file: str = DEFAULT_LOG_FILE,
    level: int = logging.INFO,
    max_bytes: int = MAX_LOG_SIZE_BYTES,
    backup_count: int = BACKUP_COUNT,
) -> logging.Logger:
    """Configures and returns a logger instance with console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if the logger is re-initialized
    if logger.handlers:
        return logger

    # Ensure target directory exists
    os.makedirs(DEFAULT_LOG_DIR, exist_ok=True)
    log_path = os.path.join(DEFAULT_LOG_DIR, log_file)

    # Standardized format for tracking crypto engine operations
    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler for real-time stdout output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Rotating file handler to manage log size
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger


# Pre-configured instance for quick usage across crypto modules
tracker_logger = setup_logger()
