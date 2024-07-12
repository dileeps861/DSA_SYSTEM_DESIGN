class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}
        for index, charS in enumerate(s):
            charT = t[index]
            if charS in dictS and dictS[charS] != charT:
                return False
            elif charT in dictT and dictT[charT] != charS:
                return False
            dictS[charS] = charT
            dictT[charT] = charS
        return True
