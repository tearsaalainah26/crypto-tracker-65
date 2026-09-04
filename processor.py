import time
import json
import urllib.request
import urllib.error
import logging

logger = logging.getLogger(__name__)

def fetch_crypto_data(url: str, max_retries: int = 3, backoff_factor: float = 1.5) -> dict:
    """Fetch cryptocurrency data from an external API with retry logic."""
    delay = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "CryptoTracker/1.0"})
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as err:
            logger.warning("Attempt %d failed for %s: %s", attempt, url, err)
            if attempt == max_retries:
                logger.error("Maximum retries reached for %s", url)
                raise
            time.sleep(delay)
            delay *= backoff_factor
    return {}
