class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return abs(idx)
            nums[idx] =  -nums[idx]
        return -1

            