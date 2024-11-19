class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def dfs(i, currSum, lst):
            if currSum == target:
                res.append(lst[:])
                return
            if currSum > target or i >= n:
                return

            lst.append(candidates[i])
            dfs(i + 1, currSum + candidates[i], lst)
            lst.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, currSum, lst)

        dfs(0, 0, [])

        return res
