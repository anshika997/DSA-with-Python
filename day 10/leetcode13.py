# Power of Three:
# Keep dividing the number by 3 while it is divisible.
# If the number finally becomes 1, it is a power of 3.

# Complexity

# Time: O(log₃ n)

#Space: O(1)

class Solution:
    def powerOfThree(self,n:int)->bool:
        if n <=0:
            return False
        while n%3==0:
            n//=3
        return n==1
sol=Solution()
print(sol.powerOfThree(27))  # True    

# Power of Three by recursion:

#  Complexity

# Time: O(log₃ n)

# Space: O(1)

class Solution:
    def powerOfThree(self,n:int)->bool:
        if n <= 0:
            return False
        if n==1:
            return True 
        if n%3!=0:
            return False
        return self.powerOfThree(n//3)
sol=Solution()
print(sol.powerOfThree(9))  # True
