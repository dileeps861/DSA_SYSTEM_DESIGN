class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mx_heap = []
        for num in nums:
            heappush(mx_heap, num)
            if len(mx_heap) > k:
                heappop(mx_heap)
        return mx_heap[0]