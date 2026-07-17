class Solution:
    def findErrorNums(self, nums):
        seen = set()
        duplicate = -1
        for num in nums :
            if num not in seen :
                seen.add(num)
            else :
                duplicate = num
        for i in range (1,len(nums)+1):
            if i not in seen :
                return [duplicate,i]
Solution = Solution()
print(Solution.findErrorNums([1,2,2,4]))
print(Solution.findErrorNums([1,1]))