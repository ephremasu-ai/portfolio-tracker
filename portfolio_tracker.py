import numpy as np
import yfinance as yf


class Position:
    """Represents an individual stock holding and processes its market metrics."""

    def __init__(self, ticker: str, shares: float):
        self.ticker = ticker.upper()
        self.shares = shares
        self.current_price = 0.0
        self.market_value = 0.0
        self.annualized_volatility = 0.0
        self.trend_signal = "UNKNOWN"

    def fetch_market_data(self):
        """Retrieves real-time price history and calculates risk/trend analytics."""
        ticker_obj = yf.Ticker(self.ticker)

        # Retrieve 1 year of daily historical data
        hist = ticker_obj.history(period="1y")

        if hist.empty or len(hist) < 50:
            raise ValueError(f"Insufficient market data for ticker: {self.ticker}")

        # Extract real-time market price & current market value
        self.current_price = hist["Close"].iloc[-1]
        self.market_value = self.current_price * self.shares

        # Calculate annualized volatility from log daily returns
        log_returns = np.log(hist["Close"] / hist["Close"].shift(1)).dropna()
        daily_volatility = log_returns.std()
        self.annualized_volatility = daily_volatility * np.sqrt(252)

        # Evaluate trend against the 50-day Simple Moving Average (SMA)
        sma_50 = hist["Close"].tail(50).mean()
        self.trend_signal = "BULLISH" if self.current_price > sma_50 else "BEARISH"


class Portfolio:
    """Aggregates multiple positions into a portfolio and prints risk reports."""

    def __init__(self):
        self.positions = []

    def add_position(self, position: Position):
        """Adds a position to the portfolio and triggers its live data retrieval."""
        position.fetch_market_data()
        self.positions.append(position)

    def display_dashboard(self):
        """Computes portfolio metrics and outputs the terminal dashboard."""
        total_value = sum(p.market_value for p in self.positions)

        if total_value == 0:
            print("Portfolio is empty.")
            return

        # Weighted annual portfolio volatility calculation
        weighted_volatility = sum(
            p.annualized_volatility * (p.market_value / total_value)
            for p in self.positions
        )

        print("\n" + "=" * 70)
        print("          QUANT PORTFOLIO RISK & PERFORMANCE DASHBOARD          ")
        print("=" * 70)

        for p in self.positions:
            weight = (p.market_value / total_value) * 100
            print(
                f"Ticker: {p.ticker:<5} | "
                f"Shares: {p.shares:<6.4f} | "
                f"Price: ${p.current_price:<7.2f} | "
                f"Value: ${p.market_value:<9.2f} | "
                f"Vol: {p.annualized_volatility * 100:>4.1f}% | "
                f"Signal: {p.trend_signal:<7} | "
                f"Weight: {weight:>4.1f}%"
            )

        print("-" * 70)
        print(f"Total Portfolio Value:       ${total_value:,.2f}")
        print(f"Weighted Annual Volatility:  {weighted_volatility * 100:.2f}%")
        print("=" * 70 + "\n")


def main():
    my_portfolio = Portfolio()

    # Exact position holdings
    my_portfolio.add_position(Position("VOO", 4.0886))
    my_portfolio.add_position(Position("NVDA", 1.0017))
    my_portfolio.add_position(Position("IJR", 1.1082))

    # Fetch live data and print terminal output
    my_portfolio.display_dashboard()


if __name__ == "__main__":
    main()
        
          
