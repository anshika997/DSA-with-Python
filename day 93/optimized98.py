class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        a = n *(n+1)//2
        b = sum(nums)
        return a-b 
Solution = Solution()
print(Solution.missingNumber([3,0,1])) # Output: 2
# Time complexity: O(n)
# Space complexity: O(1)