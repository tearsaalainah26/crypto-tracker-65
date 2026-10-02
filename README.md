[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# crypto-tracker-65

`crypto-tracker-65` is an asynchronous Python application designed to stream real-time cryptocurrency market trends, price spikes, and liquidity shifts across decentralized exchanges. It aggregates live WebSocket data from major pools to trigger instant console alerts and Telegram notifications based on user-defined volatility thresholds.

## Features

* **Multi-DEX Aggregation:** Streams live order book and trade data simultaneously from Uniswap v3, PancakeSwap, and Raydium.
* **Volatile Spike Detection:** Triggers customizable alerts when asset price or volume deviates by a set percentage within a 60-second rolling window.
* **Local Data Archiving:** Automatically dumps historical tick data and market depth to a local SQLite database for offline backtesting.
* **Telegram Bot Integration:** Sends formatted, instant buy/sell volume alerts directly to your specified Telegram channel.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
pip install -r requirements.txt
```

## Quick Start

Create a `config.py` or directly pass parameters to the `Tracker` module:

```python
from crypto_tracker import Tracker

# Initialize the tracker for target pairs
tracker = Tracker(
    pairs=["BTC/USDT", "ETH/USDT", "SOL/USDT"],
    threshold_percent=2.5,
    interval_seconds=60
)

# Define a callback for alert events
@tracker.on_price_spike
def handle_spike(event):
    print(f"[ALERT] {event.pair} moved {event.change}%! Current price: ${event.price}")

# Start listening to WebSocket streams
tracker.run()
```

## License

Distributed under the MIT License. See `LICENSE` for more information.