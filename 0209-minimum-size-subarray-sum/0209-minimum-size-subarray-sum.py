class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Approach: sliding window, keep moving i until sum > target, move j until it becomes <= target

        i = 0
        res = float("inf")
        sm = 0
        n = len(nums)
        for j in range(n):
            sm += nums[j]
            while sm >= target:
                if res > (j - i + 1):
                    res = j - i + 1
                sm -= nums[i]
                i += 1
        if res == float("inf"):
            res = 0
        return res
