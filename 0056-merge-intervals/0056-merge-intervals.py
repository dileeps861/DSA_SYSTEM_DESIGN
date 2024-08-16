class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sIntervals = sorted(intervals, key=lambda x: (x[0], [1]))
        res = []
        prevS, prevE = float('inf'), float('-inf')

        for s, e in sIntervals:
            if s <= prevE or prevS == float('inf'):
                prevS, prevE = min(s, prevS), max(e, prevE)
            else:
                res.append([prevS, prevE])
                prevS, prevE = s, e
        res.append([prevS, prevE])
        return res
