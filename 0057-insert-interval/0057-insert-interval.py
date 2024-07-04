class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Approach: is find a place in the list where start of the interval is the floor of the start of interval which is less than the new interval and then try to insert that interval in the list and then keep going up if there is a start date greater than the end date of the new interval so that we can merge those intervals so I think this could be done in log n time because log n time plus the overlapping intervals so I think this could be done in log n time.
        if not intervals:
            return [newInterval]

        def findBisectPoint():
            left = 0
            right = len(intervals) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if intervals[mid][0] > newInterval[0]:
                    right = mid - 1
                else:
                    left = mid + 1

            return left    
        
        # Find the correct position to insert newInterval using binary search
        pos = findBisectPoint()

        # Insert the newInterval at the found position
        intervals.insert(pos, newInterval)

        # Merge the intervals
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:  # Overlapping intervals
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged