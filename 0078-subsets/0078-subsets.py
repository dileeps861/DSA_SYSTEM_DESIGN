class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)

        def dfs(nums, i, lst):
            if i >= n:
                return
            for j in range(i, n):
                lst.append(nums[j])
                res.append(lst[:])
                dfs(nums, j + 1, lst)
                lst.pop()

        dfs(nums, 0, [])
        return res
