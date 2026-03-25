class Solution:
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        # Step 1: Transpose
        for i in range(row):
            for j in range(i+1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for k in range(row):
            matrix[k].reverse()
object = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
object.rotate(matrix)
print(matrix) # [[7,4,1],[8,5,2],[9,6,3]]