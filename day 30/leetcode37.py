class Solution:
    def sortedSquares(self,nums:list)->list:
        lst = [n*n for n in nums]
        lst.sort()
        return lst 
sol=Solution()
print(sol.sortedSquares([-1,-8,0,4,7]))