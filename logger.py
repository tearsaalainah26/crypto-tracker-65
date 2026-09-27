import logging
import sys
from typing import Optional

def setup_logger(name: str = 'crypto-tracker-65') -> logging.Logger:
    """Configures a robust logger with file and console outputs."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        try:
            file_handler = logging.FileHandler('crypto_tracker.log')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (IOError, PermissionError) as e:
            logger.error(f'failed to initialize file logging: {e}')

    return logger

def log_error(logger: logging.Logger, context: str, error: Exception) -> None:
    """Standardized logging wrapper for exception handling."""
    if isinstance(error, (ConnectionError, TimeoutError)):
        logger.warning(f'network failure in {context}: {type(error).__name__}')
    elif isinstance(error, ValueError):
        logger.error(f'invalid data format in {context}: {error}')
    else:
        logger.critical(f'unexpected system crash in {context}: {str(error)}', exc_info=True)
