class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictC = {}
        prev = 0
        res = 0
        for i, char in enumerate(s):
            if char in dictC and dictC[char] >= prev:
                res = max(res, i - prev)
                prev = dictC[char] + 1
            dictC[char] = i
            res = max(res, i - prev + 1)
        
        return res
