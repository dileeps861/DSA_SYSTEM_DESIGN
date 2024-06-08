class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated = [0] * 256
        i = 0
        j = 0
        n = len(s)
        res = 0
        while j < n:
            val = ord(s[j])
            while i < j and repeated[val] > 0:
                # print(ord(s[i]))
                repeated[ord(s[i])] -= 1
                i += 1
            repeated[val] += 1
            diff = (j-i+1)
            if res < diff:
                res = diff
            j += 1
        return res