class Solution:
    def transpose(self, matrix):

        result = []

        for j in range(len(matrix[0])):
            row = []

            for i in range(len(matrix)):
                row.append(matrix[i][j])

            result.append(row)

        return result 
Solution = Solution()
print(Solution.transpose([[1,2,3],[4,5,6],[7,8,9]]))
    