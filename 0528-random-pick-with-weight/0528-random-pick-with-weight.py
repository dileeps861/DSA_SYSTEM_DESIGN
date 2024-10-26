class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.w = w
        self.problity = 0
        for i, wg in enumerate(w):
            self.problity += wg / self.total
            self.w[i] = self.problity

    def pickIndex(self) -> int:
        rnd = random.random()
        idx = bisect.bisect_right(self.w, rnd)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
