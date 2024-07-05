class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        # Initialize the memoization table with None
        dp = [[None] * (amount + 1) for _ in range(n)]
        coins.sort()
        def countWays(i, remaining):
            # Base cases
            if remaining == 0:
                return 1
            if i >= n or remaining < 0:
                return 0
            
            # If already computed, return the stored value
            if dp[i][remaining] is not None:
                return dp[i][remaining]
            if remaining < coins[i]:
                dp[i][remaining] = 0
                return 0
            # Recursive cases: include coins[i] or skip it
            include = countWays(i, remaining - coins[i])
            exclude = countWays(i + 1, remaining)
            
            dp[i][remaining] = include + exclude
            return dp[i][remaining]
        
        return countWays(0, amount)