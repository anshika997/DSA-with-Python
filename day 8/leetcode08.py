# this is the example of recursive tree
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
sol=Solution()
print(sol.fib(8))  # Output: 21