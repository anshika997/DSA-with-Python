class Solution:
    def trigonacci(self,n:int)->int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return self.trigonacci(n-1)+self.trigonacci(n-2)+self.trigonacci(n-3)
sol=Solution()
print(sol.trigonacci(6))
    