# this function returns the nth tribonacci number
# but it is not efficient for large n due to its exponential time complexity
#complexity: O(3^n)

class Solution:
    def tribonacci(self,n:int)->int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
sol=Solution()
print(sol.tribonacci(6))
    