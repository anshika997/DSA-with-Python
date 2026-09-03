class Solution:
    def matrixReshape(self, mat, r, c):
        result = []
        if len(mat) * len(mat[0]) != r * c:
            return mat
        row = []
        for i in range (len(mat)):
            for j in range(len(mat[i])):
                row.append(mat[i][j])
                if len(row) == c:
                    result.append(row)
                    row = []
        return result
Solution = Solution()
print(Solution.matrixReshape([[1,2],[3,4]],1,4))
print(Solution.matrixReshape([[1,2],[3,4]],2,4))