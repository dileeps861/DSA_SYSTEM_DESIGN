class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated = set()
        i = 0
        j = 0
        n = len(s)
        res = 0
        while j < n:
            val = s[j]
            while val in repeated:
                repeated.remove(s[i])
                i += 1
            repeated.add(val)
            diff = (j-i+1)
            if res < diff:
                res = diff
            j += 1
        return res