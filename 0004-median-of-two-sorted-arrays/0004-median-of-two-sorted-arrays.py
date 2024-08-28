class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, m
        total = m + n
        half = (total + 1) // 2
        while left <= right:
            mid = left + (right - left) // 2
            nMid = half - mid

            mLeft = nums1[mid - 1] if mid > 0 else float("-inf")
            mRight = nums1[mid] if mid < m else float("inf")

            nLeft = nums2[nMid - 1] if nMid > 0 else float("-inf")
            nRight = nums2[nMid] if nMid < n else float("inf")

            if mLeft <= nRight and nLeft <= mRight:
                if total % 2 == 0:
                    return (max(mLeft, nLeft) + min(mRight, nRight)) / 2
                else:
                    return max(mLeft, nLeft)
            elif mLeft > nRight:
                right = mid - 1
            else:
                left = mid + 1
