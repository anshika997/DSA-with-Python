#Find power leetcode 50
class Solution:
    def findpower(self,x,n):
        # Base case
        if n==0:
            return 1
        # Recursive case
        a = self.findpower(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.findpower(x,n)
        else:
            return 1/self.findpower(x,n*(-1))


        