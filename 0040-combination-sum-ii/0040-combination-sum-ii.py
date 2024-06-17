class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(i, lst, sum):
            if sum > target:
                return
            if sum == target:
                res.append(lst[:])

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                lst.append(candidates[j])
                dfs(j + 1, lst, sum + candidates[j])
                lst.pop()
        dfs(0, [], 0)
        return res

