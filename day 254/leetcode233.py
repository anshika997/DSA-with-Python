class Solution:
    def runningSum(self, nums):
        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result
Solution = Solution()
print(Solution.runningSum([1,2,3,4]))