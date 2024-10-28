class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0
        for price in prices:
            if buy > price:
                print(price)
                profit = max(profit, sell - buy)
                buy = price
                sell = price
            else:
                sell = max(sell, price)
        profit = max(profit, sell - buy)
        return profit
