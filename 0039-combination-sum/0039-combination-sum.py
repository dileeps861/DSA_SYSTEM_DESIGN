class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def dfs(i, lst, currSum):
            if currSum == target:
                res.append(lst[:])
                return
            if currSum > target or i >= n:
                return
            # Take current num
            lst.append(candidates[i])
            dfs(i, lst, currSum + candidates[i])
            lst.pop(-1)  # backtracking the list
            while i + 1 < n and candidates[i + 1] == candidates[i]:
                # Skip the repeating nums to avoid duplicate combiantions
                i += 1
            # dont take the num
            dfs(i + 1, lst, currSum)

        dfs(0, [], 0)
        return res
