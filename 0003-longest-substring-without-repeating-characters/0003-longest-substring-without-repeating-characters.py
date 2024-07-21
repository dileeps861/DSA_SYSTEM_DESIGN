class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [-1] * 256
        res = 0
        i = 0
        for j in range(len(s)):
            char_ord = ord(s[j])
            if chars[char_ord] != -1:
                i = max(chars[char_ord] + 1, i)
            chars[char_ord] = j
            res = max(res, j - i + 1)
        return res
