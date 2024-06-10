class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                res = abs(idx)
                break
            nums[idx] =  -nums[idx]
        for i in range(len(nums))
            nums[i] = abs(nums[i])
        return res

            