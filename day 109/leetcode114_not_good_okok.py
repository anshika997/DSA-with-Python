# this is not a good solution as it uses extra space and time complexity is O(n) but the optimal solution has O(1) space and O(n) time complexity and only valid for non-negative integers

class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        freq = [0]*(n+1)
        for i in nums:
            freq[i]+=1
        for i in nums:
            if freq[i]==1:
                return i
Solution = Solution()
print(Solution.singleNumber([2,2,1]))  # Output: 1
print(Solution.singleNumber([4,1,2,1,2]))  # Output: 4