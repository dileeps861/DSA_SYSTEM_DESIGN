class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.prefix_sum = []
        self.problity = 0
        for wg in w:
            self.problity += wg / self.total
            self.prefix_sum.append(self.problity)

    def pickIndex(self) -> int:
        rnd = random.random()
        idx = bisect.bisect_right(self.prefix_sum, rnd)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
