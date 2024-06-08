class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        res = 0
        for price in prices:
            buy = min(buy, price)
            if buy == price:
                sell = buy
            sell = max(sell, price)
            res = max(sell - buy, res)

        return res
