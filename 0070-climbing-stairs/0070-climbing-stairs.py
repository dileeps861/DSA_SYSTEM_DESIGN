class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prevToPrev = 0

        for num in range(1,n+1):
            temp = prev
            prev = prev + prevToPrev
            prevToPrev = temp

        return prev