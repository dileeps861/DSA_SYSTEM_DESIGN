class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vouwelPrefix = "ma"
        words = sentence.split(" ")
        vowels = set(["a", "e", "i", "o", "u"])
        res = []
        for index, word in enumerate(words):
            lowerWord = word.lower()
            newWord = ""
            if lowerWord[0] in vowels:
                # it is for wovel
                newWord += word + vouwelPrefix
            else:
                newWord += word[1:] + word[0] + vouwelPrefix
            newWord += (index + 1) * 'a'
            res.append(newWord)

        return ' '.join(res)
