class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        setOfClosingBrackets = set()
        stackOfOpeningBrackets = []

        for index, char in enumerate(s):
            if char == "(":
                stackOfOpeningBrackets.append(index)
            elif char == ")":
                if stackOfOpeningBrackets:
                    stackOfOpeningBrackets.pop(-1)
                else:
                    setOfClosingBrackets.add(index)
        res = ""
        setOfOpeningBrackets = set(stackOfOpeningBrackets)
        for index, char in enumerate(s):
            if index in setOfClosingBrackets or index in setOfOpeningBrackets:
                continue
            else:
                res += char
        return res
