class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonically decreasing stack 
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while stack and temperatures[stack[-1]] <= temp:
                stack.pop(-1)
            
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res 
            