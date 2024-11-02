class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIdx = {}
        for idx, num in enumerate(nums):
            if num in numIdx and idx - numIdx[num] <= k:
                return True
            numIdx[num] = idx
        return False
