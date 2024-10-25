class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # can we do this with trie?
        # lets see..
        # /a, /a/b -> do is subfolder, and take the top most level, i.e. if match found stop there for that sub tree. Here as a is top level so /a is consider
        # /c/d, c/d/e -> Similarly here, so only /c/d is taken
        # /c/f and here /c/f
        
        class Trie:
            def __init__(self):
                self.children = {}
                self.isFolder = False

        # Root of the Trie
        trie = Trie()
        
        # Build the Trie
        for fol in folder:
            if fol == "/":
                continue
            dirF = fol.split("/")[1:]  # Split and skip the first empty element from "/"
            node = trie
            for part in dirF:
                if part not in node.children:
                    node.children[part] = Trie()
                node = node.children[part]
            node.isFolder = True

        # Result list to store the non-subfolder paths
        resFolders = []

        # Helper function for recursive traversal
        def dfs(node, path):
            if node.isFolder:
                resFolders.append("/" + "/".join(path))  # Rebuild path and add to result
                return  # Stop further recursion from this node

            # Recursively visit children
            for child in node.children:
                dfs(node.children[child], path + [child])

        # Start DFS from the root
        dfs(trie, [])
        
        return resFolders

