class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 2 3 4 5 2 3 2 1
        # if peak low < med similarly mid < high
        # 1 5 3 2 1
        #  if peak on left, low /mid if mid + 1 is there is it increasing? then peak on right
        # similarly mid -1 > mid
        left = 0
        n = len(arr)
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            if mid - 1 >= 0 and mid + 1 < n and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if mid - 1 >= 0 and arr[mid - 1] > arr[mid]:
                right = mid
            else:
                left = mid
        return arr[left]
