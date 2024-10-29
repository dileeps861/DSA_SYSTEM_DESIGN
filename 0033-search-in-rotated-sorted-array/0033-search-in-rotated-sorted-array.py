class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            # print(low, mid, high)
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[low]:
                # right is sorted
                if target > nums[mid] and nums[high] >= target:
                    # go right
                    low = mid + 1
                else:
                    # go left
                    high = mid - 1
            else:
                # left is sorted
                if target < nums[mid] and nums[low] <= target:
                    # go left
                    high = mid - 1
                else:
                    # go right
                    low = mid + 1
        return -1
