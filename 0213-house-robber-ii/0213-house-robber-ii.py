class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Helper function to perform the robbery on a given range of houses
        def rob_range(start, end):
            loot = nums[start]
            notLoot = 0
            for i in range(start + 1, end):
                new_loot = notLoot + nums[i]
                notLoot = max(loot, notLoot)
                loot = new_loot
            return max(loot, notLoot)

        # Calculate the max loot excluding the last house and excluding the first house
        max_loot1 = rob_range(0, len(nums) - 1)
        max_loot2 = rob_range(1, len(nums))

        # Return the maximum of both scenarios
        return max(max_loot1, max_loot2)