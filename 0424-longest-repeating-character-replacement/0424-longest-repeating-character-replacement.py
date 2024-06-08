class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        j = 0
        counts = defaultdict(int)
        maxLen = 0
        res = 0
        while j < n:
            char = s[j]
            counts[char] += 1
            if maxLen < counts[char]:
                maxLen = counts[char]
            if maxLen + k < (j - i + 1):
                counts[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        
        return res
