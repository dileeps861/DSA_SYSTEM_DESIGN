class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # brute force: on each step either remove the number or dont remove
        # 1. If removed go ahead with the rest of the numbers
        # 2. dont remove? the ensure it greater than previous
        # on eahc step check mas so far and step. like idx 3if was peak slop should be
        # on both sides
        # [1,2,3,4,5,1] => 0
        # [1,2,6,4,5,1] => 1
        # [1,7,6,4,5,1] => 1
        # [1,9,6,8,7,1] => 1
        # in two for loops check if each index item could be peak?
        # one thing sure, recursion will be needed to for combinations

        # Dynamic programming
        # O(n^2) Solution
        # for each number precompute its previous and next removal of items
        n = len(nums)
        ics = [0] * n
        des = [0] * n

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    ics[i] = max(ics[i], ics[j] + 1)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    des[i] = max(des[i], des[j] + 1)
        res = 0
        for i in range(n):
            if ics[i] > 0 and des[i] > 0:  # must have elements on both sides
                res = max(res, ics[i] + des[i] + 1)

        return n - res
