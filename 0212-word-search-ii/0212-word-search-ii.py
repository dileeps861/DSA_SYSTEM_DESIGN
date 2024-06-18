class Node:
    def __init__(self):
        self.children = {}
        self.word = None


DIRS = [[0, 1], [0, -1], [-1, 0], [1, 0]]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = self._buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in root.children:

                    char = board[i][j]
                    board[i][j] = "*"
                    self._search(root.children[char], i, j, board, res)
                    board[i][j] = char
        return res

    def _search(self, node, i, j, board, res):
        if node.word:

            res.append(node.word)
            node.word = None
        for u, v in DIRS:
            k, l = u + i, v + j
            if (
                k >= 0
                and k < len(board)
                and l >= 0
                and l < len(board[k])
                and board[k][l] in node.children
            ):
                char = board[k][l]
                board[k][l] = "*"
                self._search(node.children[char], k, l, board, res)
                board[k][l] = char

    def _buildTrie(self, words):
        root = Node()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
            node.word = word

        return root
