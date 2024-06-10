class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h == n:
            return max(piles)
        if n==1:
            return ceil(piles[0]/h)
        maxSpeed = max(piles)
        minSpeed = sum(piles) // h

        while minSpeed <= maxSpeed:
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2
            hoursNeeded = sum([ceil(pile/midSpeed) for pile in piles])

            if hoursNeeded <= h:
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1
        return minSpeed
