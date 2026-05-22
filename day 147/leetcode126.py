from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # Create adjacency list
        adj_list = [[] for _ in range(numCourses)]

        # Create indegree array
        indegrees = [0 for _ in range(numCourses)]

        # Build graph
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegrees[u] += 1

        # Queue for nodes having indegree 0
        queue = deque()

        # Store topological order
        result = []

        # Push all indegree 0 nodes
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        # BFS (Kahn's Algorithm)
        while len(queue) != 0:

            current_node = queue.popleft()

            result.append(current_node)

            for adjNode in adj_list[current_node]:

                indegrees[adjNode] -= 1

                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        # If all courses completed
        if len(result) == numCourses:
            return True

        return False
print(Solution().canFinish(2, [[1,0]])) # True
print(Solution().canFinish(2, [[1,0], [0,1]])) # False