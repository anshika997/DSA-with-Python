n = 7 
m = 8 
edges = [[1,2],[2,4],[3,4],[1,3],[3,5],[5,4],[6,7],[1,7]]
# 1 based indexing 
list = [[]for i in range (0,n+1)]
for u, v in edges :
    list[u].append(v)
    list[v].append(u)


print(list)