# crypto-tracker-65

Crypto-tracker-65 is a high-performance Python CLI tool designed to fetch and monitor real-time cryptocurrency price data from global exchanges. It provides automated tracking, threshold alerts, and concise terminal reporting for rapid market analysis.

## Features

*   **Real-time Price Engine:** Leverages the CoinGecko API to pull live market data for over 100+ cryptocurrencies with sub-second latency.
*   **Threshold Alerts:** Set custom trigger points; the application will provide native system notifications when your target assets hit a specific valuation.
*   **Historical Performance Tracking:** Generate simplified CSV logs of price movements over defined intervals for trend visualization.
*   **Resource-Efficient:** Built with asynchronous requests, ensuring minimal memory footprint while running as a background daemon.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Configure your desired coins in `config.json`, then execute the main script to start the tracking monitor:

```bash
# Monitor default list
python main.py --monitor

# Alert when Bitcoin exceeds $70,000
python main.py --ticker btc --alert 70000
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.