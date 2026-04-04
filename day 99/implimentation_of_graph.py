n = 6 #number of node 
e = 7 #number of edges
edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[5,0]] #edges of the graph 
print(n,e,edges)
# but this is not the best way to represent a graph
# we can represent a graph using an adjacency list 
adjList = []
for i in range(n):
    adjList.append([])
for edge in edges :
    x = edge[0]
    y = edge[1]
    adjList[x].append(y)
    adjList[y].append(x)
for i in range(n):
    print(i , "->",adjList[i])