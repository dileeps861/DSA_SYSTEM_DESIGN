class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        N = len(arr)

        # Initialize a 2D DP table with None, TLE
        # dp = [[None] * k for _ in range(N)]
        # def find(i):
        #     if i >= N:
        #         return 0
        #     res = float("-inf")
        #     mx = arr[i]
        #     for j in range(i, min(i + k, N)):
        #         mx = max(mx, arr[j])
        #         if dp[i][j - i] is None:
        #             dp[i][j - i] = mx * (j - i + 1) + find(j + 1)
        #         res = max(res, dp[i][j - i])

        #     return res

        dp = [-1] * N

        def find(i):
            if i >= N:
                return 0
            if dp[i] != -1:
                return dp[i]
            mx = arr[i]
            res = float("-inf")
            for j in range(i, min(i + k, N)):
                mx = max(mx, arr[j])
                res = max(res, mx * (j - i + 1) + find(j + 1))
            dp[i] = res
            return res

        return find(0)
