import logging
import sys
from typing import Optional

def setup_logger(name: str = 'crypto-tracker-65') -> logging.Logger:
    """Configures a standardized logger with robust error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        try:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        except (OSError, ValueError) as e:
            sys.stderr.write(f'failed to initialize logger: {e}\n')
            
    return logger

def safe_log_error(logger: logging.Logger, message: str, error: Optional[Exception] = None) -> None:
    """Logs errors safely ensuring program execution continues."""
    try:
        if error:
            logger.error(f'{message} | Error: {type(error).__name__} - {str(error)}')
        else:
            logger.error(message)
    except Exception as e:
        # Fallback if logging infrastructure fails entirely
        print(f'Critical logger failure: {e}', file=sys.stderr)