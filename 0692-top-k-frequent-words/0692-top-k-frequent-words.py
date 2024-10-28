class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cMap = Counter(words)
        cMapSorted = sorted(cMap.items(), key=lambda x: (-x[1], x[0]))

        return [cMapSorted[i][0] for i in range(k)]
