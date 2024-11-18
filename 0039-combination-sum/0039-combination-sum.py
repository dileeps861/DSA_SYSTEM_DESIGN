class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = set()

        def dfs(i, lst, currSum):
            if currSum == target:
                res.add(tuple(lst[:]))

            if currSum > target or i >= n:
                return
            if i == 0 or candidates[i - 1] != candidates[i]:
                # take the curr num and repeat it
                lst.append(candidates[i])
                dfs(i, lst, currSum + candidates[i])
                # take the curr num and dont repeat it
                dfs(i + 1, lst, currSum + candidates[i])
                lst.pop(-1)
            # dont take the num
            dfs(i + 1, lst, currSum)

        dfs(0, [], 0)
        return [val for val in res]
