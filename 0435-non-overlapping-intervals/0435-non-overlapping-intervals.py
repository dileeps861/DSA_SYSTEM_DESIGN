class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                res += 1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1]) # if the interval to be remove to optimize, remove the biggger one

        return res