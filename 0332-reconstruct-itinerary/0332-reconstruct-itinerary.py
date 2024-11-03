class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # to solve this since we need to construct the itenerary using all the path
        # the way I am thinking is form each node construct the edges and kind of do dfs
        # until all the edges considered.
        # Build connecting nodes using ADJ map
        # Starting from JFK take each edge and do coloring the way as is gray in current path other wise
        # white until unvisited.
        # Add all edges when no more edge left to visit to res list with space separated string of airports
        # And then sort the list and take the first elemetn to return.
        # But it is a brute force approach
        # # Build adjacency list
        # adj = defaultdict(list)
        # for src, dst in tickets:
        #     adj[src].append(dst)

        # res = []  # Will store all valid paths as strings
        # visited = set()  # Track visited edges

        # def dfs(curr, path):
        #     # If we used all tickets, add path to result
        #     if len(path) == len(tickets) + 1:
        #         res.append(" ".join(path))
        #         return

        #     # Try all possible destinations
        #     for i, next_dest in enumerate(adj[curr]):
        #         edge = (curr, next_dest, i)  # Use index to handle duplicate edges
        #         if edge not in visited:
        #             visited.add(edge)
        #             dfs(next_dest, path + [next_dest])
        #             visited.remove(edge)

        # # Start DFS from JFK
        # dfs("JFK", ["JFK"])

        # # Sort and return first path split into list
        # return min(res).split() if res else []

        # A better Approach but Still TLE

        # Build adjacency list and sort destinations
        # adj = defaultdict(list)
        # for src, dst in tickets:
        #     adj[src].append(dst)

        # # Sort destinations for lexicographical order
        # for src in adj:
        #     adj[src].sort()

        # visited = set()

        # def dfs(curr, path):
        #     # If we used all tickets, we found our result
        #     if len(path) == len(tickets) + 1:
        #         return path

        #     # Try all possible sorted destinations
        #     for i, next_dest in enumerate(adj[curr]):
        #         edge = (curr, next_dest, i)
        #         if edge not in visited:
        #             visited.add(edge)
        #             result = dfs(next_dest, path + [next_dest])
        #             if result:  # If valid path found, return it
        #                 return result
        #             visited.remove(edge)

        #     return None

        # return dfs("JFK", ["JFK"])

        # More optimization, instead of DFS what if I can just sort the tickets?
        # Like sort ticket, start from the stop JFK, take the next ticket which has jfk
        # mark ticket visited. End the visiting when no more tiocket
        # Sort tickets to ensure lexicographical order
        # Still TLE

        # tickets.sort()
        # n = len(tickets)
        # visited = [False] * n
        # path = ["JFK"]

        # def dfs(curr_airport):
        #     # If we found a valid path, return True
        #     if len(path) == n + 1:
        #         return True

        #     # Try each ticket
        #     for i in range(n):
        #         if not visited[i] and tickets[i][0] == curr_airport:
        #             # Use this ticket
        #             visited[i] = True
        #             path.append(tickets[i][1])

        #             # If we found a valid path, propagate True
        #             if dfs(tickets[i][1]):
        #                 return True

        #             # Otherwise backtrack
        #             visited[i] = False
        #             path.pop()

        #     return False

        # dfs("JFK")
        # return path

        # Most optimal Solution
        # Build graph and sort airport codes. And take each node which is sortest,
        # and if we popped we dont need to maintain visited
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for src in graph.keys():
            graph[src].sort()

        path = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop(0))
            path.append(airport)

        dfs("JFK")
        return path[::-1]
