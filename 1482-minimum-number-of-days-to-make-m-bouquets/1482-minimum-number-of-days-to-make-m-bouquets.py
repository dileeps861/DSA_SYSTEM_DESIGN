class Solution:
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1
        low, high = min(bloomDay), max(bloomDay)
        def canMakeBouquets(days):
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False
        while low <= high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low