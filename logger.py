import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = 'crypto-tracker-65') -> logging.Logger:
    """Initializes application-wide logger with rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler with 5MB rotation limit
    file_handler = RotatingFileHandler(
        'tracker.log', 
        maxBytes=5*1024*1024, 
        backupCount=2
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Global logger instance for consistency across modules
app_logger = setup_logger()