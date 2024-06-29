class Solution:
    def rob(self, nums: List[int]) -> int:
        
        loot = nums[0]
        notLoot = 0
        for i in range(1, len(nums)):
            loot, notLoot = notLoot + nums[i], max(loot, notLoot)
        return max(loot, notLoot)        