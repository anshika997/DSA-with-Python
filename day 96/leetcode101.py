class Solution:
    def mark_infinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(0, r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")

        for j in range(0, c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix):
        r = len(matrix)      # ✅ FIX
        c = len(matrix[0])   # ✅ FIX

        # Step 1: mark infinity
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    self.mark_infinity(matrix, i, j)

        # Step 2: convert infinity to 0
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == float("inf"):   # ✅ FIX
                    matrix[i][j] = 0
Solution = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution.setZeroes(matrix)
print(matrix) # Output: [[1,0,1],[0,0,0],[1,0,1]]
