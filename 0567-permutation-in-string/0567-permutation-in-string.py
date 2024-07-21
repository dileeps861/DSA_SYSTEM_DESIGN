class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charsMap1 = [0] * 26
        for char in s1:
            ordChar = ord(char) - ord("a")
            charsMap1[ordChar] += 1

        charsMap = [0] * 26
        i = 0
        for j in range(len(s2)):
            ordChar = ord(s2[j]) - ord("a")
            charsMap[ordChar] += 1

            while charsMap[ordChar] > charsMap1[ordChar] and i <= j:
                ordChar_i = ord(s2[i]) - ord("a")
                charsMap[ordChar_i] -= 1
                i += 1

            if j >= i and (j - i + 1) == len(s1):
                if eq(charsMap, charsMap1):
                    return True
        return False
