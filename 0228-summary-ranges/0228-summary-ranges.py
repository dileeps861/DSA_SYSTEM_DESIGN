class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        left = 0
        right = 0

        def makeDes():
            if left != right:
                res.append(str(nums[left]) + "->" + str(nums[right]))
            else:
                res.append(str(nums[left]))

        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[right] + 1:
                right = i
            else:
                makeDes()
                left = i
                right = i
        makeDes()
        return res
