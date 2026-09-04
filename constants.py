import logging

# Configuration constants for crypto-tracker-65
# Includes safe default values and error message strings

API_TIMEOUT_SECONDS = 30
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5

HTTP_STATUS_MESSAGES = {
    400: "Bad request: Check input parameters.",
    401: "Unauthorized: API key invalid.",
    403: "Forbidden: Access denied to exchange.",
    404: "Not found: Endpoint does not exist.",
    429: "Rate limit exceeded: Please slow down requests.",
    500: "Internal server error: Exchange services unstable.",
    503: "Service unavailable: Server is currently overloaded."
}

SUPPORTED_EXCHANGES = ['binance', 'coinbase', 'kraken']
DEFAULT_CURRENCY = 'USD'

def get_error_message(status_code: int) -> str:
    """Returns descriptive message for standard HTTP status codes."""
    return HTTP_STATUS_MESSAGES.get(status_code, "Unknown API connection error occurred.")

# Configure global logging settings for monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('crypto-tracker-65')