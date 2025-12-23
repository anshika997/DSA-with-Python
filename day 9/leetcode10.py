# with the help of bitwise operator 
class solution:
    def ispoweroftwo(self,n: int)->bool:
        if n<=0:
            return False
        return (n&(n-1))==0
sol = solution()
print(sol.ispoweroftwo(16))

# without bitwise operator
# With recursion
class solution:
    def isPowerOfTwo(self,n:int)->bool:
        
        if n==0:
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        return self.isPowerOfTwo(n//2)
sol=solution()
print(sol.isPowerOfTwo(32))

# without recursion
#With loop 
class solution:
    def isPowerOfTwo(self,n:int)->bool:
        if n>0:
            return False
        while n%2==0:
            n//=2
        return n==1
sol=solution()
print(sol.isPowerOfTwo(18))
    
# we can also do this with if-else
#if n==1:
#     return True
# else:
#     return False
