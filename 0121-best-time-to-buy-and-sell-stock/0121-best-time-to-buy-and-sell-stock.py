class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        sell = float("-inf")
        res = 0
        for price in prices:
            buy = min(buy, price)
            if buy == price:
                sell = float("-inf")
            sell = max(sell, price)
            res = max(sell - buy, res)

        return res
