class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        loot = nums[0]
        notLoot = 0
        for i in range(1, len(nums) - 1):
            loot, notLoot = notLoot + nums[i], max(loot, notLoot)
        res = max(loot, notLoot)        

        loot = nums[1]
        notLoot = 0
        for i in range(2, len(nums)):
            loot, notLoot = notLoot + nums[i], max(loot, notLoot)
        res = max(res, max(loot, notLoot))        
        return res