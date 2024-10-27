class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add num and idx
        n = len(temperatures)
        res = [0] * n

        ms = []
        for i in range(n - 1, -1, -1):
            while ms and temperatures[ms[-1]] <= temperatures[i]:
                ms.pop()
            if ms:
                idx = ms[-1]
                res[i] = idx - i
            ms.append(i)

        return res
