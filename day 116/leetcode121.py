class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [0]*n
        def DFS(node):
            visited[node]=1
            for n in rooms[node]:
                if visited[n]==0:
                    DFS(n)
        DFS(0)
        return all(visited)
Solution=Solution()
print(Solution.canVisitAllRooms([[1],[2],[3],[]]))
print(Solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
