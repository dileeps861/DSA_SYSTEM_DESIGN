class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        explored = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in explored:
                return [explored[complement], index]
            explored[num] = index
        return []