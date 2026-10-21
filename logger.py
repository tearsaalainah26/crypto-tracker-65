import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str = "crypto_tracker",
    log_file: str = "logs/tracker.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3
) -> logging.Logger:
    """Configures and returns a logger with console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if logger.hasHandlers():
        return logger

    log_formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create log directory if it does not exist
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # File output handler with log rotation
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    return logger


# Default logger instance for the crypto tracker core
tracker_logger = setup_logger()
