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

        # build rest of the ( exck
        for val in stack:
            dict_map[val] = True

        return ''.join(char for i, char in enumerate(s) if i not in dict_map)
