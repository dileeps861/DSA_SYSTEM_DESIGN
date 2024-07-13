class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dictOfChar = {}
        for index, char in enumerate(order):
            dictOfChar[char] = index

        custom = []

        count = len(order)

        for char in s:
            if char in dictOfChar:
                custom.append((dictOfChar[char], char))
            else:
                custom.append((count, char))
                count += 1
        custom.sort()
        custom = [x[1] for x in custom]
        return "".join(custom)