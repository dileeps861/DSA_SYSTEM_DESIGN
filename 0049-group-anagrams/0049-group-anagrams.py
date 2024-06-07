class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            countSter = tuple(count)
            
            res[countSter].append(word)
        finalRes = []
        for key, value in res.items():
            finalRes.append(value)

        return finalRes