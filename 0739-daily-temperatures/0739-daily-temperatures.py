class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add num and idx
        res = [0] * len(temperatures)
        i = len(temperatures) - 1
        ms = []
        while i >= 0:
            while ms and ms[-1][0] <= temperatures[i]:
                ms.pop(-1)
            if ms:
                temp, idx = ms[-1]
                res[i] = idx - i
            ms.append((temperatures[i], i))
            i -= 1

        return res
