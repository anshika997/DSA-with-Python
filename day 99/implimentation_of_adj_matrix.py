# adjacency matrix implementation of graph
n = 6 # number of nodes 
edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[5,0]]  # number of edges 
adjMatrix = [] 
for i in range (n):
    adjMatrix.append([-1]*n)
for edge in edges :
    x = edge[0]
    y = edge[1]
    
# print(adjMatrix)
    adjMatrix[x][y] = 1
    adjMatrix[y][x] = 1
for i in adjMatrix:
    print(i)
    
    