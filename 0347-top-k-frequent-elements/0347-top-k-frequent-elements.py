class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        numCount = Counter(nums)
        pq = []
        for num, count in numCount.items():
            heappush(pq, (count, num))
            if len(pq) > k:
                heappop(pq)
        res = []
        while pq:
            res.append(heappop(pq)[1])
        return res

