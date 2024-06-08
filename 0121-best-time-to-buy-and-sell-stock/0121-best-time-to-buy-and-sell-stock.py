class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        j = 0
        buy = float("inf")
        sell = float("-inf")
        res = 0
        while j < len(prices):
            buy = min(buy, prices[j])
            if buy == prices[j]:
                sell = float("-inf")
            sell = max(sell, prices[j])
            res = max(sell - buy, res)
            j += 1
        return res
