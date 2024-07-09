class StockPrice:

    def __init__(self):
        from sortedcontainers import SortedDict
        self.stockPrices = SortedDict()
        self.sortedPrice = SortedDict()
        self.latestTime = 0

    def update(self, timestamp: int, price: int) -> None:
        # print(timestamp, price)
        if timestamp in self.stockPrices:
            old = self.stockPrices[timestamp]
            if self.sortedPrice[old] > 1:
                self.sortedPrice[old] = self.sortedPrice[old] - 1
            else:
                del self.sortedPrice[old]
        if price not in self.sortedPrice:
            self.sortedPrice[price] = 0
        self.sortedPrice[price] = self.sortedPrice[price] + 1
        self.stockPrices[timestamp] = price
        self.latestTime = max(self.latestTime, timestamp)

    def current(self) -> int:
        # print("curr:", self.stockPrices.peekitem(-1)[0])
        return self.stockPrices[self.latestTime]

    def maximum(self) -> int:
        return self.sortedPrice.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.sortedPrice.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()