class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        right = 0
        jump = nums[0] - 1
        for right in range(1, n):
            if jump < 0:
                return False
            if nums[right] > jump:
                jump = nums[right]
            jump -= 1
            
        return True
