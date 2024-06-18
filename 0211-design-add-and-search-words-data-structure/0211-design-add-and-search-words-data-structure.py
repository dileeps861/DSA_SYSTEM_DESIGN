class Node:
    def __init__(self):
        self.children = dict()
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        self.isWord = False

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        ans = [False]
        self._search(self.root, word, 0, ans)
        return ans[0]

    def _search(self, node, word, i, ans):
        if i == len(word):
            if node and node.isWord:
                ans[0] = True
            return
        char = word[i]
        if char == ".":
            for key, val in node.children.items():
                self._search(val, word, i + 1, ans)
        elif char in node.children:
            self._search(node.children[char], word, i + 1, ans)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
