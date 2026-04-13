from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()

        # Add all 0 cells to queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = 1

        directions = [(-1,0), (0,-1), (0,1), (1,0)]

        # BFS
        while queue:
            i, j, d = queue.popleft()
            distance[i][j] = d

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy

                if (0 <= new_i < rows and 
                    0 <= new_j < cols and 
                    visited[new_i][new_j] == 0):

                    visited[new_i][new_j] = 1
                    queue.append((new_i, new_j, d + 1))

        return distance


# 🔽 Example run (for VS Code testing)
if __name__ == "__main__":
    mat = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]

    sol = Solution()
    result = sol.updateMatrix(mat)

    for row in result:
        print(row)