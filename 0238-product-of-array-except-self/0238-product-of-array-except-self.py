class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        suffixProd = [1] * (len(nums) + 1)
        for i in range(len(nums)-1, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i]
        prev = 1
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = prev * suffixProd[i+1]
            prev = prev * temp
        return nums
