class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        dict_map = set()
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    dict_map.add(i)
            elif s[i] == "(":
                stack.append(i)

        # build rest of the ( exck
        dict_map.update(stack)

        res = []

        for i in range(len(s)):
            if i in dict_map:
                continue
            else:
                res.append(s[i])
        return ''.join(res)
