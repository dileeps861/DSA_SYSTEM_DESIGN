from bisect import bisect_left

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Why not greedy? 1,4,5 -> 12, greedy: 2*5 + 2*1 = 4 coins, but way is 3*4 =12 -> 3coins

        # So need to check all the possible ways and get the best answer
        # DP way is store the cost to make n = k amount ox x coin the n-k coins + x coin
        # O(n^2) tc and sc =O(n) to store previous counts
        n = len(coins)
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            index = bisect_left(coins, i)
            if index == len(coins):  # Reduce index by 1 if it is out of bounds
                    index -= 1
            while index >= 0:
                coin = coins[index]
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
                index -= 1
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]

