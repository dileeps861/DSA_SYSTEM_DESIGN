class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        prev = nums[0]
        while j < len(nums):
            if nums[j] != prev:
                i += 1
                nums[i] = nums[j]
                prev = nums[j]
            j += 1
        return i + 1
