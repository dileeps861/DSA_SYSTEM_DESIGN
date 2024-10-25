class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        pq = []
        for start, end in intervals:
            if not pq:
                pq.append([start, end])
            else:
                if pq[-1][1] >= start:
                    s, e = pq.pop(-1)
                    pq.append([min(start, s), max(end, e)])
                else:
                    pq.append([start, end])

        return pq
