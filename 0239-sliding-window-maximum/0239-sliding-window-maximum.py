from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []

        dq = deque()
        res = []

        for i in range(n):
            # Remove elements not within the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements smaller than the current element from the deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add the current element's index to the deque
            dq.append(i)

            # Append the current max to the result list once the first window is complete
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
