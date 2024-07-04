class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
                prev_end = min(prev_end, intervals[i][1]) # if the interval to be remove to optimize, remove the biggger one
            else:
                prev_end = intervals[i][1]

        return res