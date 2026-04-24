class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2
        
        for i in range(3, n+1):
            a, b = b, a + b
        
        return b
Solution = Solution()
print(Solution.climbStairs(2))
print(Solution.climbStairs(3))
print(Solution.climbStairs(4))
print(Solution.climbStairs(5))