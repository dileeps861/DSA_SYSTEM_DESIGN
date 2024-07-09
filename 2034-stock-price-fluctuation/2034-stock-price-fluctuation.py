from sortedcontainers import SortedDict

class StockPrice:
    def __init__(self):
        self.stockPrices = SortedDict()  # Stores prices by timestamp.
        self.sortedPrice = SortedDict()  # Stores frequency of each price.

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.stockPrices:
            old_price = self.stockPrices[timestamp]
            # Decrease the count of the old price. If it hits zero, remove it.
            if self.sortedPrice[old_price] == 1:
                del self.sortedPrice[old_price]
            else:
                self.sortedPrice[old_price] -= 1
        
        # Set the new price in both dictionaries.
        self.stockPrices[timestamp] = price
        if price in self.sortedPrice:
            self.sortedPrice[price] += 1
        else:
            self.sortedPrice[price] = 1

    def current(self) -> int:
        # Return the most recent price. peekitem(-1) returns (key, value).
        return self.stockPrices.peekitem(-1)[1]

    def maximum(self) -> int:
        # Return the largest price. peekitem(-1) returns (key, value).
        return self.sortedPrice.peekitem(-1)[0]

    def minimum(self) -> int:
        # Return the smallest price. peekitem(0) returns (key, value).
        return self.sortedPrice.peekitem(0)[0]
