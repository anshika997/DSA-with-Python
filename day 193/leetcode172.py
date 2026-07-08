import math 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = math.sqrt(num)
# here we are checking whether it is whole number or note 
        if sqrt % 1  ==  0 :
            return True 
        else :
            return False
Solution = Solution()
print(Solution.isPerfectSquare(16))
print(Solution.isPerfectSquare(14))
print(Solution.isPerfectSquare(25))