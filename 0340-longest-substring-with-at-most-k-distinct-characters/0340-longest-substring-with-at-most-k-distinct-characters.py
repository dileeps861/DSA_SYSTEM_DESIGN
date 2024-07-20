class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        sDict = {}

        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] not in sDict:
                sDict[s[j]] = 0
            sDict[s[j]] += 1

            while len(sDict) > k:
                charI = s[i]
                if sDict[charI] == 1:
                    del sDict[charI]
                else:
                    sDict[charI] -= 1
                i += 1
            res = max(res, (j - i + 1))
        return res
