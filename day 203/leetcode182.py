class Solution:
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        s = set(nums)
        result = []
        for i in range (1,n+1):
            if i not in s:
                result.append(i)
        return result
Solution = Solution()
print(Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(Solution.findDisappearedNumbers([1,1]))