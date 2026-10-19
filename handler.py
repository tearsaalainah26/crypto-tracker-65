import logging

def validate_crypto_payload(data):
    """Ensures payload contains valid ticker and volume fields."""
    required_fields = {'ticker', 'volume'}
    if not isinstance(data, dict):
        return False
    if not required_fields.issubset(data.keys()):
        return False
    if not isinstance(data['ticker'], str) or not isinstance(data['volume'], (int, float)):
        return False
    if data['volume'] <= 0:
        return False
    return True

def process_stream(data_stream):
    """Main loop for processing incoming crypto data packets."""
    logger = logging.getLogger(__name__)
    for packet in data_stream:
        try:
            if not validate_crypto_payload(packet):
                logger.warning(f"Invalid packet structure received: {packet}")
                continue
            
            ticker = packet['ticker'].upper()
            volume = float(packet['volume'])
            
            # Processing logic for verified crypto data
            print(f"Processing transaction: {ticker} @ {volume}")
            
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Processing error: {e}")
            continue

if __name__ == '__main__':
    # Simulation of incoming data stream
    sample_data = [
        {'ticker': 'BTC', 'volume': 0.5},
        {'ticker': 'ETH', 'volume': -10}, 
        {'invalid': 'data'}
    ]
    process_stream(sample_data)