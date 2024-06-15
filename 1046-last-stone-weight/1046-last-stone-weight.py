class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
    
        while len(max_heap) > 1:
            x = heappop(max_heap)
            y = heappop(max_heap)

            if x == y:
                continue
            elif x < y:
                heappush(max_heap, (x - y))
            else:
                heappush(max_heap, (y - x))
        if len(max_heap) == 0:
            return 0
        return -max_heap[0]
