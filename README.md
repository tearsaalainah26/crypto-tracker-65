[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# crypto-tracker-65

`crypto-tracker-65` is an asynchronous Python library and CLI tool designed for real-time cryptocurrency price monitoring across major exchanges via low-latency WebSocket feeds. It aggregates live order book snapshots, tracks portfolio performance, and triggers automated alerts when custom market conditions are met.

## Features

* **Multi-Exchange Streaming:** Connects concurrently to Binance, Coinbase, and Kraken WebSockets to stream tick-level price data.
* **Custom Alert Triggers:** Configurable threshold engine for desktop and webhook notifications on price movements, RSI divergence, or volume spikes.
* **Local PnL Tracking:** Automatically computes real-time portfolio profit/loss against historical purchase data stored in a lightweight local SQLite database.
* **Structured Data Export:** Dumps raw price streams and aggregated OHLCV candles to JSON or CSV for offline technical analysis.

## Installation

Ensure you have Python 3.9+ installed on your system.

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
pip install -r requirements.txt
python setup.py install
```

## Quick Start

### Basic CLI Usage

Track live pairs directly from your terminal:

```bash
crypto-tracker --pairs BTC/USDT ETH/USDT --exchange binance --interval 5s
```

### Python API Example

Integrate real-time monitoring into your own Python scripts:

```python
import asyncio
from crypto_tracker import MarketMonitor

async def main():
    # Initialize monitor for specified trading pairs
    monitor = MarketMonitor(pairs=["BTC/USDT", "ETH/USDT"], exchange="binance")

    # Set an automated alert for price thresholds
    monitor.add_alert(pair="BTC/USDT", target_price=65000.00, direction="above")

    # Start streaming live market data
    async for tick in monitor.stream():
        print(f"[{tick.timestamp}] {tick.pair}: ${tick.price:,.2f}")

if __name__ == "__main__":
    asyncio.run(main())
```

## License

This project is licensed under the [MIT License](LICENSE).