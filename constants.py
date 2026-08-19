API_ENDPOINT = 'https://api.cryptoservice.com'

RATE_LIMIT = 60  # requests per minute

DEFAULT_CURRENCY = 'USD'

SUPPORTED_CURRENCIES = [
    'BTC', 'ETH', 'LTC', 'XRP', 'ADA', 'DOT'
]

ERROR_MESSAGES = {
    'network_error': 'Network issues, please try again later.',
    'invalid_currency': 'The provided currency is not supported.',
    'rate_limit_exceeded': 'You have exceeded the rate limit. Please wait and try again.'
}

# Timing constants
REQUEST_TIMEOUT = 10  # seconds
CACHE_EXPIRY = 300  # seconds
