class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        dict_map = {}
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if stack:
                    stack.pop(-1)
                else:
                    dict_map[i] = True
            elif s[i] == "(":
                stack.append(i)

        # build rest of the ( exclusion
        for val in stack:
            dict_map[val] = True

        res = ""

        for i in range(len(s)):
            if i in dict_map:
                continue
            else:
                res += s[i]
        return res
