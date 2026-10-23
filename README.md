[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# crypto-tracker-65

`crypto-tracker-65` is an asynchronous Python client designed to stream real-time market data and calculate portfolio valuations across multiple cryptocurrency exchanges. It monitors price fluctuations, aggregates order book depth, and triggers customizable alerts directly to your terminal or webhook endpoints.

## Features

- **Multi-Exchange Streaming:** Unified WebSocket interface for continuous price feeds from Binance, Coinbase, and Kraken.
- **Custom Volatility Alerts:** Threshold-based notifications for sudden price swings, volume spikes, and unusual gas fee movements.
- **Historical Data Caching:** Automated SQLite logging for OHLCV candles to support offline strategy backtesting.
- **Async Overhead:** Built on `asyncio` and `aiohttp` for low-latency processing and minimal system resource usage.

## Installation

Clone the repository and install the dependencies using `pip`:

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
pip install -r requirements.txt
```

## Quick Start

Create a `config.json` with your monitored pairs or run the async tracker directly in your Python code:

```python
import asyncio
from crypto_tracker import TrackerEngine

async def monitor_market():
    # Initialize tracker for target assets
    tracker = TrackerEngine(pairs=["BTC/USDT", "ETH/USDT"], exchange="binance")
    
    print("Starting live ticker stream...")
    async for ticker in tracker.stream_tickers():
        print(f"[{ticker.exchange}] {ticker.pair}: ${ticker.price:,.2f} | 24h Vol: {ticker.volume_24h}")

if __name__ == "__main__":
    asyncio.run(monitor_market())
```

Run via CLI to output formatted tracking logs:

```bash
python -m crypto_tracker --pairs BTC/USDT ETH/USDT --interval 5s
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.