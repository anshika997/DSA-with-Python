# This function returns all elements of a 2D matrix in spiral order.
# Spiral order means:
# 1. Traverse the top row from left to right
# 2. Traverse the right column from top to bottom
# 3. Traverse the bottom row from right to left
# 4. Traverse the left column from bottom to top
# This process continues layer by layer until all elements are visited.
# Time Complexity: O(n × m) because each matrix element is visited once.
# Space Complexity: O(n × m) due to the output list storing all elements.

class solution:
    def spiralmatrix(self,matrix:list[list[int]])->int:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        total = n*m
        c = 0
        colstart=0
        colend=m-1
        rowstart=0
        rowend=n-1
        while c<total:
            # rowstart,colstart->colend
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                c+=1
            rowstart+=1
            if c==total:
                break
            #colend,rowstart->rowend

            for i in range(rowstart,rowend+1):
                ans.append(matrix[i][colend])
                c+=1
            colend-=1
            if c==total:
                break
            # rowend,colend->colstart
            for i in range(colend,colstart-1,-1):
                ans.append(matrix[rowend][i])
                c+=1
            rowend-=1
            if c==total:
                break
            # colstart,rowend->rowstart
            for i in range(rowend,rowstart-1,-1):
                ans.append(matrix[i][colstart])
                c+=1
            colstart+=1
            if c==total:
                break
        return ans
sol=solution()
print(sol.spiralmatrix([[1,2,3],[4,5,6],[7,8,9]]))
        
        

        
            
            
                    