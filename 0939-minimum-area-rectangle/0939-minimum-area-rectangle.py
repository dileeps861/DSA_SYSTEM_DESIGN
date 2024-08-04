class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dictPoinsts = defaultdict(set)

        for point in points:
            dictPoinsts[point[0]].add(point[1])
            # dictPoinsts[point[1]].add(point[0])

        minArea = float("inf")
        for i in range(len(points)):
            for j in range(0, i):
                # consider this is diagonal
                # find anti diagonal points
                p1 = points[i]
                p2 = points[j]

                if (
                    p1[0] != p2[0]
                    and p1[1] != p2[1]
                ):
                    if (
                        p1[0] in dictPoinsts
                        and p2[1] in dictPoinsts[p1[0]]
                        and p2[0] in dictPoinsts
                        and p1[1] in dictPoinsts[p2[0]]
                    ):
                        area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])  # Fixed line
                        minArea = min(minArea, area)
        return minArea if minArea != float("inf") else 0