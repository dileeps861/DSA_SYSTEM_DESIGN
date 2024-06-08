class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Map = Counter(s1)
        i = 0
        s2Map = defaultdict(int)
        for j in range(len(s2)):
            s2Map[s2[j]] += 1
            while i <j and s2[j] not in s1Map or s2Map[s2[j]] > s1Map[s2[j]]:
                s2Map[s2[i]] -= 1
                i += 1
            if (j - i + 1) == len(s1):
                # print(s2Map, i, j)
                return True
        return False
