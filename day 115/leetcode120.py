from collections import deque
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [0]*(n)
        def bfs_graph(starting_node):
            queue = deque()
            queue.append(starting_node)
            visited[starting_node] = 1

            while len(queue)!=0:
                e = queue.popleft()
                # ans.append(e)

                for node in range(n) :
                    if isConnected[e][node]==1 and visited[node]==0:
                        queue.append(node)
                        visited[node]=1
        count = 0 

        for i in range(n):
            if visited[i]==0:
                bfs_graph(i)
                count+=1
        return count
Solution = Solution()
print(Solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
print(Solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))