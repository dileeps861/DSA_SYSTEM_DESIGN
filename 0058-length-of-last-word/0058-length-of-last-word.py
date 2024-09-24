class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        tmp = 0
        for char in s:
            if char == ' ':
                if tmp:
                    res = tmp
                    tmp = 0
            else:
                tmp += 1
        if tmp:
            res = tmp
        return res
