class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars_count = {}

        def putToDict(key, val):
            if key not in chars_count:
                chars_count[key] = 0
            chars_count[key] += val

        def delFrom(key, val):
            if chars_count[key] == 1:
                del chars_count[key]
            else:
                chars_count[key] -= val

        i = 0
        res = 0
        for j in range(len(s)):
            char = s[j]
            putToDict(char, 1)
            while len(chars_count) > 2:
                delFrom(s[i], 1)
                i += 1
            res = max(j - i + 1, res)
        return res
