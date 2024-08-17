class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        prev = nums[i]
        while j < len(nums):
            if prev != nums[j]:
                nums[i] = prev
                i += 1
                prev = nums[j]
            j += 1
        nums[i] = prev
        i += 1

        return i
