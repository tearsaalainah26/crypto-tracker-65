import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str = "crypto_tracker",
    log_file: str = "crypto_tracker.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3,
) -> logging.Logger:
    """Configures and returns a logger with console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear any pre-existing handlers to avoid duplication
    if logger.hasHandlers():
        logger.handlers.clear()

    # Ensure directory structure for the log file exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Standard format containing time, log level, and component trace
    log_format = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Rolling disk logging handler
    try:
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except OSError as e:
        logger.error(f"Failed to configure rotating file output: {e}")

    return logger


if __name__ == "__main__":
    # Simple local smoke test
    tracker_log = setup_logger(log_file="logs/app_runtime.log")
    tracker_log.info("Crypto feed parsing system startup succeeded")
    tracker_log.warning("Binance API returned high network latency (420ms)")
