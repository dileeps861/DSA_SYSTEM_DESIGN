class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    #     total = sum(nums)
    #     if total % 2 != 0:
    #         return False
    #     target = total // 2

    #     @lru_cache(maxsize=None)
    #     def dfs(i, curr_sum):
    #         if curr_sum == target:
    #             return True
    #         if i >= len(nums) or curr_sum > target:
    #             return False
    #         # take or skip
    #         return dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)

    #     return dfs(0, 0)

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        # dp[i] = True if a subset sum of i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # 0 is always possible

        for num in nums:
            # Traverse backwards to avoid using the same num multiple times
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]