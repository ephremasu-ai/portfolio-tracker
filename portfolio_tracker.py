class Portfolio:
    def __init__(self, stock, weight, cost):
        self.stock = stock
        self.weight = weight  
        self.cost = cost
    def __str__(self):
        return f"Portfolio: Stock {self.stock}| Weight: {self.weight}| Cost {self.cost}"
    def heat_map(self):
        if self.weight < 30 and self.weight > 0:
            color = "red"
        else:
            color = "green"
        return color
    def selection_stock(self):
        self.stock_selection = []
        if not self.stock_selection:
            self.stock_selection.extend(["VOO", "QQQM", "VTI"])
        return self.stock_selection
def main():
    Holdings_1 = Portfolio("Nvidia", 24.3, 182.67)
    Holdings_2 = Portfolio("VOO", 56.2, 634.32)
    print(Holdings_1)
    print(Holdings_2)
    print(f"Holdings 1 Heatmap: {Holdings_1.heat_map()}")
    print(f"Holdings 2 Heatmap: {Holdings_2.heat_map()}")
    Holdings_1.selection_stock()
    print(f"Selection List: {Holdings_1.stock_selection}")
if __name__ == '__main__':
    main()
        
