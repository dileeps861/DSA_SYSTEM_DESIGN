class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Pointer for the place to put the next non-val element
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
