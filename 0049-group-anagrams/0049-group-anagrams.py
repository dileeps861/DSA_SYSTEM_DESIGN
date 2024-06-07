class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            st = tuple(sorted(word))
            res[st].append(word)
        finalRes = []
        for key, value in res.items():
            finalRes.append(value)

        return finalRes