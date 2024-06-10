class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = i + (j-i) // 2
            val = nums[mid]
            if val == target:
                return mid

            if val > target:
                j = mid - 1 
            else:
                i = mid + 1
        return -1