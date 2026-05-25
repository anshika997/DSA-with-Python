import sys

def findTheCity(n, edges, distanceThreshold):

    # Create adjacency matrix
    adj_matrix = [[sys.maxsize for _ in range(n)] for _ in range(n)]

    # Fill edges
    for u, v, w in edges:
        adj_matrix[u][v] = w
        adj_matrix[v][u] = w

    # Distance from node to itself = 0
    for i in range(n):
        adj_matrix[i][i] = 0

    # Floyd Warshall Algorithm
    for via in range(n):

        for i in range(n):

            for j in range(n):

                if adj_matrix[i][via] != sys.maxsize and adj_matrix[via][j] != sys.maxsize:

                    adj_matrix[i][j] = min(
                        adj_matrix[i][j],
                        adj_matrix[i][via] + adj_matrix[via][j]
                    )

    min_neigh = n
    city = -1

    # Count reachable cities
    for i in range(n):

        count = 0

        for j in range(n):

            if adj_matrix[i][j] <= distanceThreshold:
                count += 1

        # Choose city with minimum neighbors
        # If tie -> larger city number
        if count <= min_neigh:
            min_neigh = count
            city = i

    return city


# Driver Code
n = 4

edges = [
    [0,1,3],
    [1,2,1],
    [1,3,4],
    [2,3,1]
]

distanceThreshold = 4

print(findTheCity(n, edges, distanceThreshold))