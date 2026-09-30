# Quantitative Portfolio Tracker & Risk Engine

An Object-Oriented Python application designed to track real-time stock positions, evaluate market trend signals, and compute portfolio-level annualized volatility metrics using `yfinance` and `numpy`.

## Key Features
- **Object-Oriented Architecture**: Modular `Position` and `Portfolio` classes managing holdings, allocations, and data aggregation.
- **Live Market Data Integration**: Fetches real-time prices and historical price series directly via the Yahoo Finance API (`yfinance`).
- **Quant Risk Metrics**: Calculates annualized log-return volatility ($\sigma_{ann} = \sigma_{daily} \times \sqrt{252}$).
- **Trend Following Signals**: Evaluates current prices against a 50-day Simple Moving Average (SMA) to classify positions as BULLISH or BEARISH.

## Technologies Used
- Python 3.x
- NumPy (Vectorized quantitative math)
- yfinance (Financial market data retrieval)

## How It Works
```python
from portfolio_tracker import Portfolio, Position

# Instantiate portfolio and add positions
my_portfolio = Portfolio()
my_portfolio.add_position(Position("VOO", 4.0))
my_portfolio.add_position(Position("NVDA", 1.0))

# Output aggregated risk dashboard
my_portfolio.display_dashboard()
Portfolio: Stock Nvidia| Weight: 24.3| Cost 182.67
Portfolio: Stock VOO| Weight: 56.2| Cost 634.32
Holdings 1 Heatmap: red
Holdings 2 Heatmap: green
Selection List: ['VOO', 'QQQM', 'VTI']

