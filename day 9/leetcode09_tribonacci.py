# the time complexity of this code is O(n)
# space complexity is O(1)
# this is more efficient than the previous recursive approach

class Solution:
    def tribonacci(self,n:int)->int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a,b,c=0,1,1
        for i in range(3,n+1):
            
# we take n+1 because we want to include n in our loop and generally range function excludes the last number
#  a,b,c=b,c,a+b+c we can also do this in one line
            
            d= a+b+c
            a,b,c=b,c,d
        return c
sol= Solution()
print(sol.tribonacci(6))

           