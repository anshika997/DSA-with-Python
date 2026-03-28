# brute force approach
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(0, n + 1):
            if i not in nums:
                return i
Solution = Solution()
print(Solution.missingNumber([3,0,1]))
print(Solution.missingNumber([0,1]))