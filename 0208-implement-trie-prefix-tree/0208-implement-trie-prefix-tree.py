class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node("*")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self._searchNode(word)
        return node is not None and node.isWord

    def startsWith(self, prefix: str) -> bool:
        return self._searchNode(prefix) is not None

    def _searchNode(self, prefix: str) -> Node:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
