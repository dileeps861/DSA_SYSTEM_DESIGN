class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            new_i = i
            while nums[i] != i + 1:
                target = nums[i] - 1          # where nums[i] belongs
                if nums[target] == nums[i]:   # duplicate found
                    return nums[i]
                nums[i], nums[target] = nums[target], nums[i]  # swap into place
            
        # print(nums)
        return nums[- 1]
