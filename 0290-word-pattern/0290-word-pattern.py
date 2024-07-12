class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordsDict = {}
        charDict = {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for index, char in enumerate(pattern):
            if char in wordsDict or words[index] in charDict:
                if (char in wordsDict and wordsDict[char] != words[index]) or (words[index] in charDict and charDict[words[index]] != char):
                    return False
            else:
                wordsDict[char] = words[index]
                charDict[words[index]] = char
        return True
