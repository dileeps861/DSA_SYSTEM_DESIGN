class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # First sq range
        x1, x2 = rec1[0], rec1[2]
        y1, y2 = rec1[1], rec1[3]

        # second sq range
        x3, x4 = rec2[0], rec2[2]
        y3, y4 = rec2[1], rec2[3]

        # check if overlapping
        if x1 < x3 < x2 or x3 < x1 < x4 or x1 < x4 < x2 or x3 < x2 < x4:
            if y1 < y3 < y2 or y3 < y1 < y4 or y1 < y4 < y2 or y3 < y2 < y4:
                return True
        return False
