class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res
Solution = Solution()
print(Solution.reverse(123))       # Output: 321
print(Solution.reverse(-123))      # Output: -321
print(Solution.reverse(120))       # Output: 21
print(Solution.reverse(0))         # Output: 0
print(Solution.reverse(1534236469))  # Output: 0 (because the
# reversed integer overflows)