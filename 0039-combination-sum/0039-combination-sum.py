class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def dfs(candidates, i, sum, lst):
            if i >= n or sum > target:
                return
            for j in range(i, n):
                lst.append(candidates[j])
                total = sum + candidates[j]
                if  total == target:
                    res.append(lst[:])
                dfs(candidates, j, total, lst)
                lst.pop()
        dfs(candidates, 0, 0, [])
        return res
            
