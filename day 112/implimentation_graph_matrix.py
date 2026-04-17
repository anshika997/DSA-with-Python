# this i how we can store graph in the form of matrix


n = 6
m = 7 
edges = [[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]] 
# 1 based indexing 
matrix = [[0 for _ in range(0,n+1)] for _ in range(0,n+1)]
# print(matrix)
for u,v in edges :
    matrix[u][v] = 1 
    matrix[v][u] = 1 
print(matrix)
    
 
