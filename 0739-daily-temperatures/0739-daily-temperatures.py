class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add num and idx
        res = [0] * len(temperatures)
        i = len(temperatures) - 1
        ms = []
        while i >= 0:
            while ms and temperatures[ms[-1]] <= temperatures[i]:
                ms.pop()
            if ms:
                idx = ms[-1]
                res[i] = idx - i
            ms.append(i)
            i -= 1

        return res
