class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # sort intervals by the start time
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # if overlapping intervals then merge them
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res
