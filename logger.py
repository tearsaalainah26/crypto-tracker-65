import logging
import sys
from typing import Any

# Configure crypto-tracker-65 logging infrastructure
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('crypto-tracker-65')

def log_error(exception: Exception, context: str = "") -> None:
    """Logs edge case exceptions with stack trace information."""
    error_msg = f"Error in {context}: {str(exception)}" if context else str(exception)
    
    if isinstance(exception, (ConnectionError, TimeoutError)):
        logger.warning(f"Network transient error: {error_msg}")
    elif isinstance(exception, ValueError):
        logger.error(f"Invalid data input: {error_msg}")
    else:
        logger.critical(f"Unexpected system failure: {error_msg}", exc_info=True)

def log_data_anomaly(metric: str, value: Any) -> None:
    """Records unusual crypto market data for audit."""
    logger.warning(f"Market anomaly detected: {metric} has invalid value: {value}")