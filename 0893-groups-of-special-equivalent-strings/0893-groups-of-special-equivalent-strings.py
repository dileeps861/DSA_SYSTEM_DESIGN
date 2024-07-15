class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def countChar(word):
            even_idx_chars = [0] * 26
            odd_idx_chars = [0] * 26

            for idx, char in enumerate(word):
                if idx % 2 == 0:
                    even_idx_chars[ord(char) - ord('a')] += 1
                else:
                    odd_idx_chars[ord(char) - ord('a')] += 1
            return (tuple(even_idx_chars), tuple(odd_idx_chars))

        equivalent = set()
        for word in words:
            tpl = countChar(word)
            equivalent.add(tpl)
        return len(equivalent)
