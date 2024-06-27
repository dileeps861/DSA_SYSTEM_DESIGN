class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        n = len(nums)

        # Brute force O(n^2)
        # for i in range(n):
        #     currSum = 0
        #     for j in range(i, n):
        #         currSum += nums[j]
        #         res = max(res, currSum)

        #  Optimal solution, start left=right = 0
        # keep moving forward and if the total sum becomes less than nums[right] upon adding new element and reset total sum = nums[right] otherwise add nums to totalSum
        right = 0
        totalSum = 0
        while right < n:
            if totalSum + nums[right] < nums[right]:
                totalSum = 0
            totalSum += nums[right]
            res = max(res, totalSum)
            right += 1

        return res