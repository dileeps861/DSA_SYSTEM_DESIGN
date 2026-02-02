class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     num = nums[i]
        #     while nums[i] != i + 1:
        #         target = nums[i] - 1          # where nums[i] belongs
        #         if nums[target] == nums[i]:   # duplicate found
        #             return nums[i]
        #         nums[i], nums[target] = nums[target], nums[i]  # swap into place

        # # print(nums)

        # return nums[- 1]

        for i in range(len(nums)):
            j = abs(nums[i]) - 1      # use abs in case nums[i] was already negated
            if nums[j] < 0:
                return j + 1           # j+1 is the duplicate value
            nums[j] = -1 * nums[j]
        return -1