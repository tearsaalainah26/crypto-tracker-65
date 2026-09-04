import logging
import os
import sys
from typing import Optional


def setup_logger(
    name: str = "crypto_tracker",
    log_file: Optional[str] = None,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configure and return a standard logger for the crypto tracker.

    This logger formats messages with timestamps, log levels, and module names.
    If a log file path is provided, it will also log to that file.

    Args:
        name: The name of the logger instance.
        log_file: Optional file path to write log messages.
        level: The logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if the logger is already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (if specified)
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
