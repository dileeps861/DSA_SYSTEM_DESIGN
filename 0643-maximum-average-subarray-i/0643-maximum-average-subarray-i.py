class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliidng window approach

        i = 0
        j = 0
        res = float('-inf')
        sumSoFar = 0
        while j < len(nums):
            sumSoFar += nums[j]
            j += 1
            if j - i < k:
                continue
            else:
                avg = sumSoFar / k
                if res < avg:
                    res = avg
                sumSoFar -= nums[i]
                i += 1
        return res
