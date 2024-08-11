class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def buildGraph():
            adj = defaultdict(set)
            for a, b in prerequisites:
                adj[b].add(a)
            return adj

        adj = buildGraph()
        visited = defaultdict(int)
        res = [True]

        def dfs(node):
            stack = []
            stack.append(node)
            while stack:
                nodePoped = stack[-1]
                if visited[nodePoped] == 0:  # If unvisited, start processing
                    visited[nodePoped] = 2  # Mark as visiting
                flag = True
                for nT in adj[nodePoped]:
                    if visited[nT] == 2:
                        res[0] = False
                        return

                    if visited[nT] == 0:
                        flag = False
                        stack.append(nT)
                        
                if flag:
                    stack.pop(-1)
                    visited[nodePoped] = 3

        for n in range(numCourses):
            if not res[0]:
                return False
            dfs(n)
        return res[0]
