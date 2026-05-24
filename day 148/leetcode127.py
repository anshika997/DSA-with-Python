from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):

        n = len(graph)

        # Reverse graph
        reverse_graph = [[] for _ in range(n)]

        # Indegree array
        indegree = [0] * n

        # Build reverse graph
        for u in range(n):
            for v in graph[u]:

                reverse_graph[v].append(u)

                indegree[u] += 1

        # Queue for terminal nodes
        queue = deque()

        # Nodes with indegree 0
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        safe = []

        # BFS
        while queue:

            node = queue.popleft()

            safe.append(node)

            for neighbor in reverse_graph[node]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe)
print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) # [2,4,5,6]    
print(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])) # [4]