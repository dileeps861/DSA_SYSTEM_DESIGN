class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # first sort the number 
        # get total sum
        # if total odd return immidiatl false
        # at any point if we have curr sum == total//2 return true
        # at any point we have two choices, take ith number of skipp it
        nums.sort()
        total = sum(nums)
        half = total // 2
        n = len(nums)
        if total % 2 != 0:
            return False
        # dp = [None for _ in range(n)]
        # def findPartition(i, currSum):
        #     if i >= n:
        #         if currSum == half:
        #             return True
        #         return False
        #     if currSum == half:
        #         dp[i][currSum] = True
        #         return True
        #     if currSum > half:
        #         return False
        #     if dp[i][currSum] != None:
        #         return dp[i][currSum]
        #     dp[i][currSum] = findPartition(i+1, currSum + nums[i]) or findPartition(i+1, currSum)
        #     return dp[i][currSum]
        # return findPartition(0, 0)

        # Furthure optimization: We can optimize space as all we need to know is with given sum
        # is it possible to make res sum

        dp = [False] * (half + 1)
        dp[0] = True
        
        # Update the DP array
        for num in nums:
            for j in range(half, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[half]
