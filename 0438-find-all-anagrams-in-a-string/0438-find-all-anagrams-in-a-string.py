class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pMap = [0] * 26
        for char in p:
            charOrd = ord(char) - ord('a')
            pMap[charOrd] += 1

        res = []
        i = 0
        sMap = [0] * 26
        for j in range(len(s)):
            charOrd = ord(s[j]) - ord('a')
            sMap[charOrd] += 1 
            while sMap[charOrd] > pMap[charOrd] and i <= j:
                charOrdI = ord(s[i]) - ord('a')
                sMap[charOrdI] -= 1 
                i += 1
            if sMap == pMap:
                res.append(i)
        return res
