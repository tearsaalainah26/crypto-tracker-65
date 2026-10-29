from functools import lru_cache
import re

# regex pattern for cryptocurrency symbol validation
SYMBOL_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')

@lru_cache(maxsize=128)
def validate_ticker(symbol: str) -> bool:
    """verify crypto ticker format using cached results"""
    if not isinstance(symbol, str):
        return False
    return bool(SYMBOL_PATTERN.match(symbol.strip().upper()))

def batch_validate_tickers(symbols: list[str]) -> list[str]:
    """efficient validation of list of symbols"""
    return [s for s in symbols if validate_ticker(s)]

class DataValidator:
    """performance-oriented validator for crypto price packets"""
    def __init__(self, required_fields: tuple = ('price', 'symbol', 'ts')):
        self.required_fields = set(required_fields)

    def is_valid_packet(self, data: dict) -> bool:
        """fast schema verification using set intersection"""
        if not isinstance(data, dict):
            return False
        
        # verify required fields existence
        if not self.required_fields.issubset(data.keys()):
            return False
            
        # validate symbol content
        return validate_ticker(data['symbol'])
