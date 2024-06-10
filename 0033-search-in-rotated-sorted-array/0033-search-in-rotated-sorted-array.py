class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,8,9,0,1,2] t = 0
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            midVal = nums[mid]
            if midVal == target:
                return mid
            if midVal >= nums[low] and midVal >= nums[mid - 1]:
                # print(nums)
                # print(mid, midVal, target,low, high)
                if mid - 1 >= 0 and target <= nums[mid - 1] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if mid + 1 < len(nums) and target >= nums[mid + 1] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
