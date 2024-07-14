class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:

            if char == ")":
                words = []
                while stack[-1] != "(":
                    words.append(stack.pop(-1))
                stack.pop(-1)
                stack.extend(words)
            else:
                stack.append(char)
        return "".join(stack)
