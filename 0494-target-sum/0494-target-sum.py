class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def findWays(i, currSum):
            if i == n:
                if currSum == target:
                    return 1
                return 0

            tp = (i, currSum)
            if tp in dp:
                return dp[tp]

            dp[tp] = findWays(i + 1, currSum + nums[i]) + findWays(i + 1, currSum - nums[i])
            return dp[tp]

        return findWays(0, 0)
