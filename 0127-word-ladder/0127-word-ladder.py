class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return
        # make set
        st = set(wordList)
        # Using a list comprehension
        alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        result = 1
        while q:
            sz = len(q)
            while sz > 0:
                word = q.popleft()
                if word == endWord:
                    return result
                # iterate through each char
                for i in range(len(word)):
                    prefix = word[:i]
                    suffix = word[i + 1:]
                    # then try replacing each cha between a-z
                    for ch in alphabet:
                        newWord = prefix + str(ch) + suffix
                        if newWord in st and newWord not in visited:
                            q.append(newWord)
                            visited.add(newWord)
                sz -= 1
            result += 1
        return 0
