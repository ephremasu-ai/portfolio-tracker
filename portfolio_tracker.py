import numpy as np
import yfinance as yf

class Position:
    def __init__(self, ticker: str, shares: float):
        self.ticker = ticker
        self.shares = shares
        self.price = 0.0
        self.value = 0.0
        self.volatility = 0.0
        self.signal = "N/A"
        self.update_market_data()

    def update_market_data(self):
        t = yf.Ticker(self.ticker)
        self.price = t.fast_info['lastPrice']
        self.value = self.shares * self.price
        
        hist = t.history(period="6m")['Close']
        returns = np.log(hist / hist.shift(1)).dropna()
        
        self.volatility = np.std(returns) * np.sqrt(252)
        
        sma_50 = hist.tail(50).mean()
        self.signal = "BULLISH" if self.price > sma_50 else "BEARISH"

    def __str__(self):
        return (f"Ticker: {self.ticker:<5} | Shares: {self.shares:<6.2f} | "
                f"Price: ${self.price:<7.2f} | Value: ${self.value:<9.2f} | "
                f"Vol: {self.volatility*100:<5.1f}% | Signal: {self.signal}")


class Portfolio:
    def __init__(self):
        self.positions = []

    def add_position(self, position: Position):
        self.positions.append(position)

    def total_value(self) -> float:
        return sum(pos.value for pos in self.positions)

    def get_portfolio_volatility(self) -> float:
        total = self.total_value()
        if total == 0:
            return 0.0
        return sum((pos.value / total) * pos.volatility for pos in self.positions)

    def display_dashboard(self):
        print("=" * 70)
        print("          QUANT PORTFOLIO RISK & PERFORMANCE DASHBOARD           ")
        print("=" * 70)
        
        tot_val = self.total_value()
        for pos in self.positions:
            weight = (pos.value / tot_val) * 100 if tot_val > 0 else 0
            print(f"{pos} | Weight: {weight:.1f}%")

        print("-" * 70)
        print(f"Total Portfolio Value:       ${tot_val:,.2f}")
        print(f"Weighted Annual Volatility:  {self.get_portfolio_volatility()*100:.2f}%")
        print("=" * 70)


def main():
    my_portfolio = Portfolio()
    
    my_portfolio.add_position(Position("VOO", 4.0781))
    my_portfolio.add_position(Position("NVDA", 1.0017))
    my_portfolio.add_position(Position("IJR", 1.1082))

    my_portfolio.display_dashboard()


if __name__ == "__main__":
    main()
