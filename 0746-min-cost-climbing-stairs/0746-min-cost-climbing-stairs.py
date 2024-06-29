class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        prevToPrev = 0
        n = len(cost)
        for i in range(0,n):
            temp = prev
            prev = min(prev, prevToPrev) + cost[i]
            prevToPrev = temp
        return min(prev, prevToPrev)