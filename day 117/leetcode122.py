class Solution:
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            ans.append(bin(i).count('1'))
        return ans
Solution = Solution()
print(Solution.countBits(5))
print(Solution.countBits(2))