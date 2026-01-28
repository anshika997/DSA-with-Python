class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0 
        r = rows*cols -1
        
        while l <=r:
            mid = (l+r)//2
            # find the coordinate of row
            i = mid//cols
            # finds the coordinate of column 
            j = mid%cols
            if matrix[i][j]==target :
                return True 
            elif matrix[i][j] > target:
                # left shift the r
                r = mid-1
            else:
                # right shift the l 
                l = mid+1
        return False
sol= Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)) 
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)) 


        