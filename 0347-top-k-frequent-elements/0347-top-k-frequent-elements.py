class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for key, val in count.items():
            heappush(res,(val, key))
            if len(res) > k:
                heappop(res)
        
        return [val for c, val in res]
