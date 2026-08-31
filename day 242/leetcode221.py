class Solution:
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid//len(matrix[0])
            col = mid%len(matrix[0])

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target :
                right = mid-1

            else:
                left = mid+1

        return False
Solution = Solution()
print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))