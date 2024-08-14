class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bisectLeft(low, high):
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        def bisectRight(low, high):
            while low <= high:
                mid = low + (high - low) // 2  # This ensures that mid is always rounded up, which is necessary for the right bound search.
                if nums[mid] <= target:
                    low = mid + 1  # Needed for convergence
                else:
                    high = mid - 1
            return high

        low, high = 0, len(nums) - 1

        left, right = bisectLeft(low, high), bisectRight(low, high)
        if 0 <= left <= high and nums[left] == target:
            return [left, right]
        return [-1, -1]
