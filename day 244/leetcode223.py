class Solution:
    def diagonalSum(self, mat) :
        n = len(mat)
        middle = 0
        result = 0 
        if n%2  != 0:
            middle = mat[n//2][n//2]
        for i in range(len(mat)):
            result += mat[i][i]
        for i in range(len(mat)) :
            result += mat[i][n-1-i]
        result = result-middle
        return result
Solution = Solution()
print(Solution.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))