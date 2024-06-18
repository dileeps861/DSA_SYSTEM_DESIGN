class Node:
    def __init__(self, val):
        self.val = val
        self.childern = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node("*")

    def insert(self, word: str) -> None:
        i = 0
        node = self.root
        while i < len(word):
            char = word[i]
            if char not in node.childern:
                node.childern[char] = Node(char)
            node = node.childern[char]
            i += 1
        node.isWord = True

    def search(self, word: str) -> bool:
        i = 0
        node = self.root
        while i < len(word):
            char = word[i]
            if char not in node.childern:
                return False
            node = node.childern[char]
            i += 1
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        i = 0
        node = self.root
        while i < len(prefix):
            char = prefix[i]
            if char not in node.childern:
                return False
            node = node.childern[char]
            i += 1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
