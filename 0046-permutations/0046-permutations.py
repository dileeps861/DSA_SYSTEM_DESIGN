class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(nums, i):
            if i >= n:
                res.append(nums[:])
                return
            
            for j in range(i, n):
                nums[j], nums[i] = nums[i], nums[j]
                dfs(nums, i + 1)
                nums[j], nums[i] = nums[i], nums[j]
              
        dfs(nums, 0)
        return res
            