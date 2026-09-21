# crypto-tracker-65

Crypto-tracker-65 is a high-performance Python utility designed to monitor real-time cryptocurrency price fluctuations across multiple exchanges. It provides actionable data insights for traders looking to track portfolio performance and market volatility with minimal latency.

## Features

*   **Multi-Exchange Integration:** Aggregates live price feeds from Binance, Coinbase, and Kraken via REST and WebSocket APIs.
*   **Automated Alerting:** Configurable threshold triggers that send desktop notifications when assets hit specific price targets.
*   **Portfolio Snapshot:** Calculates total asset valuation in real-time, accounting for holding quantities and base currency conversion.
*   **CSV Data Logging:** Automatically archives price history to local storage for retrospective technical analysis and trend modeling.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/crypto-tracker-65.git
cd crypto-tracker-65
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

To start tracking your primary assets, update the `config.yaml` file with your desired trading pairs and run the main entry point:

```bash
# Track default assets listed in config.yaml
python main.py --monitor

# View a one-time snapshot of the current market
python main.py --snapshot BTC,ETH,SOL
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.