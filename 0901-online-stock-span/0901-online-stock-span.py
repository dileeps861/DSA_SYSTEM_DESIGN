class StockSpanner:

    def __init__(self):
        self.stackOfNumsCount = []

    def next(self, price: int) -> int:
        span = 0

        while self.stackOfNumsCount and self.stackOfNumsCount[-1][0] <= price:
            prevPrice, prevSpan = self.stackOfNumsCount.pop(-1)
            span += prevSpan
        span += 1
        self.stackOfNumsCount.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
