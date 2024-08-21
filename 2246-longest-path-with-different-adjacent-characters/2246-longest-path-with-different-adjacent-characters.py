class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        from collections import defaultdict

        # Build parent to children dictionary
        parent_to_children = defaultdict(list)
        for child, p in enumerate(parent):
            if p != -1:
                parent_to_children[p].append((child, s[child]))

        res = [1]
        
        def dfs(node):
            if node not in parent_to_children:
                return 1
            longest = 0
            secondLongest = 0

            for child, char in parent_to_children[node]:
                lengthF = dfs(child)
                if s[node] != char:
                    if lengthF > longest:
                        secondLongest = longest
                        longest = lengthF
                    elif lengthF > secondLongest:
                        secondLongest = lengthF

            res[0] = max(res[0], longest + secondLongest + 1)
            return longest + 1

        dfs(0)
        return res[0]
