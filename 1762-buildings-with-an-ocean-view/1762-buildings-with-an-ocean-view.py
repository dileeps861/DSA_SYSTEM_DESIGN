class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        j = len(heights) - 1
        res = []
        mx = 0
        while j >= 0:
            if heights[j] > mx:
                res.append(j)
            if mx < heights[j]:
                mx = heights[j]
            j -= 1
        return res[::-1]
