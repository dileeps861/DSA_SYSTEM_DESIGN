class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        index = 0
        sign = 1
        num = 0

        if s[index] in ['-', '+']:
            sign = -1 if s[index] == '-' else 1
            index += 1

        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])

            if num * sign >= INT_MAX:
                return INT_MAX
            if num * sign <= INT_MIN:
                return INT_MIN

            index += 1

        return num * sign