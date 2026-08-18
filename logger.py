import logging
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:
    """
    Set up a logger with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler(f'{name}.log')
    file_handler.setLevel(logging.DEBUG)

    # Create formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger


def log_event(logger: logging.Logger, event: str, level: str = 'info') -> None:
    """
    Log an event with the specified level.

    Args:
        logger (logging.Logger): The logger instance to log the event to.
        event (str): The event message to log.
        level (str): The logging level ('debug', 'info', 'warning', 'error', 'critical'). Default is 'info'.
    """
    log_function = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical,
    }.

    log_function.get(level, logger.info)(event)
