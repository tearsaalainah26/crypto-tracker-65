# crypto-tracker-65

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command-line cryptocurrency tracker built in Python for monitoring digital asset prices and portfolio performance. It fetches real-time market data to help users stay informed about their investments without relying on web interfaces.

## Features

- Retrieves live prices for over 100 cryptocurrencies via the CoinGecko API
- Calculates portfolio value based on user-defined holdings and current market rates
- Sets and monitors price alerts for specific coins with console notifications
- Displays 24-hour price changes and basic trend indicators

## Installation

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
pip install -r requirements.txt
```

## Usage

Track prices for selected cryptocurrencies:

```bash
python main.py BTC ETH SOL
```

Load a portfolio from a JSON file to view total value:

```bash
python main.py --portfolio portfolio.json
```

Set a price alert for a specific coin:

```bash
python main.py --alert BTC 45000
```

## License

MIT License