class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # n = len(nums)
        # dp = [1] * n  # Initialize DP array with 1s because the minimum LIS is 1 (each element by itself)
        # res = 1
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #             res = max(res, dp[i])
        # return res

        # further optimization use binary search
        import bisect
        lisList = []
        for num in nums:
            if not lisList:
                lisList.append(num)
                continue
            idx = bisect.bisect_left(lisList, num)
            if idx == len(lisList):
                lisList.append(num)
            else:
                lisList[idx] = num
        return len(lisList)
