class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        mn = 101
        for val in nums:
            if mn > val:
                mn = val
            counts[val] = True
        if mn < k:
            return -1
        if mn == k:
            return len(counts) - 1
        else:
            return len(counts)
