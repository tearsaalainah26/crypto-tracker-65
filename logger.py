import logging
import sys
from typing import Optional


class CryptoTrackerLogger:
    """Custom logger wrapper for crypto market monitoring and alerting."""

    def __init__(
        self, name: str = "crypto_tracker", log_level: int = logging.INFO
    ) -> None:
        """Initialize the logger with standard output and formatting.

        Args:
            name: The module or component name for the logger.
            log_level: Numeric logging level (e.g., logging.INFO, logging.DEBUG).
        """
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            handler: logging.Handler = logging.StreamHandler(sys.stdout)
            formatter: logging.Formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log_price_alert(
        self, symbol: str, price: float, threshold: float
    ) -> None:
        """Log a price threshold breach for a specific cryptocurrency.

        Args:
            symbol: Ticker symbol of the asset (e.g., BTC, ETH).
            price: Current market price of the asset.
            threshold: The target price threshold that was crossed.
        """
        self.logger.warning(
            f"ALERT: {symbol.upper()} crossed threshold! Current: ${price:,.2f} | Threshold: ${threshold:,.2f}"
        )

    def log_api_status(
        self, endpoint: str, status_code: int, response_time_ms: float
    ) -> None:
        """Log execution metrics for external exchange API calls.

        Args:
            endpoint: API endpoint URL or route name.
            status_code: HTTP response status code.
            response_time_ms: Response time in milliseconds.
        """
        msg: str = f"API Call: {endpoint} | Status: {status_code} | Latency: {response_time_ms:.1f}ms"
        if status_code >= 400:
            self.logger.error(msg)
        else:
            self.logger.info(msg)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Utility function to retrieve a configured logger instance.

    Args:
        name: Optional logger name suffix.

    Returns:
        Configured logging.Logger object.
    """
    logger_name: str = f"crypto_tracker.{name}" if name else "crypto_tracker"
    return CryptoTrackerLogger(logger_name).logger
