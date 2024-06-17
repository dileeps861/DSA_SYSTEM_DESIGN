class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def dfs(nums, i, lst):
            res.append(lst[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                lst.append(nums[j])
                dfs(nums, j + 1, lst)
                lst.pop()
        dfs(nums, 0, [])
        return res
        