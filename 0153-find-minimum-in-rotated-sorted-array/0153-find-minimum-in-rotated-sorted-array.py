class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while True:
            mid = low + (high - low) // 2
            midVal = nums[mid]
            if nums[low] <= midVal and midVal <= nums[high]:
                return nums[low]
            if mid == low and mid == high:
                print(mid)
                return nums[mid]
            if midVal >= nums[low] and midVal >= nums[mid - 1]:
                low = mid + 1
            else:
                high = mid
        return 0
