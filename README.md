# crypto-tracker-65

Crypto-tracker-65 is a high-performance Python utility designed to monitor real-time cryptocurrency price fluctuations and historical data trends. It provides developers and traders with a lightweight interface to track portfolio assets directly from the command line.

## Features

*   **Real-time Price Engine:** Fetches live price data via the CoinGecko API with optimized asynchronous requests.
*   **Custom Portfolio Alerts:** Configurable price thresholds that trigger desktop notifications when assets hit target values.
*   **Historical Analysis:** Generates terminal-based Sparkline charts to visualize 24-hour price trends.
*   **CSV Exporting:** Automated logging functionality to track portfolio performance over time in structured CSV files.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

To start tracking your favorite assets, simply provide the ticker symbols as arguments:

```bash
# Track Bitcoin and Ethereum prices
python tracker.py --assets BTC ETH

# Set a price alert for BTC at $60,000
python tracker.py --assets BTC --alert 60000
```

The script will poll the market every 60 seconds by default. To view the full list of configuration options and market commands, run:

```bash
python tracker.py --help
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the `LICENSE` file for details.