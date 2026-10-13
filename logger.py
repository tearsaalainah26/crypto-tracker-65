import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "crypto_tracker.log", level: int = logging.INFO) -> logging.Logger:
    """Configures a logger with console and file output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File output
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def log_exception(logger: logging.Logger, error: Exception, context: str = ""): 
    """Utility for standardized exception reporting."""
    msg = f"Error occurred in {context}: {str(error)}" if context else f"Error: {str(error)}"
    logger.error(msg, exc_info=True)