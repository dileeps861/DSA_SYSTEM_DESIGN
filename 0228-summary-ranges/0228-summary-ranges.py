class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        left = 0
        right = 0
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[right] + 1:
                right = i
            else:
                if left != right:
                    res.append(str(nums[left]) + "->" + str(nums[right]))
                else:
                    res.append(str(nums[left]))
                left = i
                right = i
        if left != right:
            res.append(str(nums[left]) + "->" + str(nums[right]))
        else:
            res.append(str(nums[left]))
        return res
