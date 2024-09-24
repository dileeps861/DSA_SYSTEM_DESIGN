class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        i = 0
        # Add all intervals that come before the new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge all overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1

        # Add the merged interval (or the new interval if no merge happened)
        res.append(newInterval)

        # Add the remaining intervals after the new interval
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
