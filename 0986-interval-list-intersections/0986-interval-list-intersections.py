class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first = 0
        second = 0
        m = len(firstList)
        n = len(secondList)
        result = []
        while first < m and second < n:
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])

            if end >= start:
                result.append([start, end])
                
            if secondList[second][1] < firstList[first][1]:
                second += 1
            else:
                first += 1
        return result