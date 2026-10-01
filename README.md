# Quantitative Portfolio Risk & Performance Tracker

An object-oriented Python application that tracks stock portfolio positions, fetches real-time market data via `yfinance`, and computes core quantitative risk and trend metrics.

---

## Key Features

- **Real-Time Market Data Integration:** Fetches historical daily prices dynamically using `yfinance`.
- **Quantitative Risk Analytics:** Computes annualized log-return volatility scaled by trading days ($\sqrt{252}$).
- **Trend Identification:** Evaluates position signals against a 50-day Simple Moving Average (SMA).
- **Portfolio Aggregation:** Calculates weighted portfolio volatility and position weights.
- **Terminal Dashboard:** Formatted ASCII table summarizing current holdings and portfolio-level analytics.

---

## Holdings

The tracker defaults to the following portfolio configuration:

| Ticker | Asset Description | Position Size |
| :--- | :--- | :--- |
| **VOO** | Vanguard S&P 500 ETF | 4.0886 shares |
| **NVDA** | NVIDIA Corporation | 1.0017 shares |
| **IJR** | iShares Core S&P Small-Cap ETF | 1.1082 shares |

---

Note: Output generated dynamically at runtime based on real-time Yahoo Finance market data.

Plaintext
======================================================================
          QUANT PORTFOLIO RISK & PERFORMANCE DASHBOARD          
======================================================================
Ticker: VOO   | Shares: 4.0886 | Price: $700.86 | Value: $2,865.54 | Vol: 11.2% | Signal: BULLISH | Weight: 88.3%
Ticker: NVDA  | Shares: 1.0017 | Price: $228.38 | Value: $228.77   | Vol: 42.1% | Signal: BULLISH | Weight:  7.1%
Ticker: IJR   | Shares: 1.1082 | Price: $136.04 | Value: $150.76   | Vol: 16.5% | Signal: BULLISH | Weight:  4.6%
----------------------------------------------------------------------
Total Portfolio Value:       $3,245.07
Weighted Annual Volatility:  13.63%
======================================================================


