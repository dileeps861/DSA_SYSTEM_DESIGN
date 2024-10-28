class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cMap = Counter(words)
        cMapSorted = sorted(cMap.items(), key=lambda x: (-x[1], x[0]))
        print(cMapSorted)
        i = 0
        res = []
        while i < k and len(res) < k:
            res.append(cMapSorted[i][0])
            i += 1

        return res
