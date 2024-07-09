class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        toRemove = set()
        for idx, char in enumerate(s):
            if char == ')':
                if not stack:
                    toRemove.add(idx)
                else:
                    stack.pop()
            elif char == '(':
                stack.append(idx)
        toRemove.update(stack)

        # Construct the result by skipping indices in toRemove
        return ''.join(char for idx, char in enumerate(s) if idx not in toRemove)
