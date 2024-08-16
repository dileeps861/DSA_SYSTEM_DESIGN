class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        sortedFreq = sorted(freq.items(), key=lambda x: (-x[1], [0]))
        return map(lambda x: x[0], sortedFreq[:k])