import logging

def validate_crypto_data(data):
    """Validates incoming dictionary for crypto-tracker-65 constraints."""
    required_fields = {'symbol', 'price', 'volume'}
    
    if not isinstance(data, dict):
        return False
        
    if not required_fields.issubset(data.keys()):
        return False
        
    if not isinstance(data['price'], (int, float)) or data['price'] < 0:
        return False
        
    if not isinstance(data['symbol'], str) or len(data['symbol']) < 2:
        return False
        
    return True

def run_processing_loop(data_stream):
    """Main loop for processing crypto ticker updates."""
    logger = logging.getLogger('crypto-tracker-65')
    
    for entry in data_stream:
        try:
            if not validate_crypto_data(entry):
                logger.warning(f"Invalid data packet skipped: {entry}")
                continue
                
            # Process valid ticker data
            symbol = entry['symbol'].upper()
            price = entry['price']
            logger.info(f"Processing {symbol} at {price}")
            
        except Exception as e:
            logger.error(f"Unexpected error in processing loop: {e}")
            continue