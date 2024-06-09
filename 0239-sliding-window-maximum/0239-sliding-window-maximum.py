class Solution:    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        # Max-heap for the current window
        pq = []
        res = []
        
        # Initialize the heap with the first window
        for i in range(k):
            heappush(pq, (-nums[i], i))
        
        res.append(-pq[0][0])
        
        for i in range(k, n):
            # Add the new element to the heap
            heappush(pq, (-nums[i], i))
            
            # Remove the elements not within the window
            while pq[0][1] <= i - k:
                heappop(pq)
            
            # The current max is the root of the heap
            res.append(-pq[0][0])
        
        return res