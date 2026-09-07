class Solution:
    def oddCells(self, m,n,indices):

        matrix = [[0] * n for _ in range(m)]

        for row, col in indices:

            for j in range(n):
                matrix[row][j] += 1

            for i in range(m):
                matrix[i][col] += 1

        result = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    result += 1

        return result
Solution = Solution()
print(Solution.oddCells(2,3,[[0,1],[1,1]]))