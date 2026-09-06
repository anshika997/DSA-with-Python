class Solution:
    def luckyNumbers(self, mat) :
        result = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == min(mat[i]) and mat[i][j] == max(mat[k][j] for k in range(len(mat))):
                    result.append(mat[i][j])
        return result
Solution = Solution()
print(Solution.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))