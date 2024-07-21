class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        res = 0
        zerosCount = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zerosCount += 1
            while zerosCount > k:
                if nums[i] == 0:
                    zerosCount -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
