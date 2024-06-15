class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointClose = []
        for point in points:
            dist = -sqrt(point[0]**2+point[1]**2)
            heappush(pointClose, [dist, point])
            if len(pointClose) > k:
                heappop(pointClose)
        return [point for dist, point in pointClose]
            

