class Solution:
    def runningSum(self, nums) :
        result = []

        total = 0

        for i in range(len(nums)):
            total += nums[i]
            result.append(total)

        return result
Solution = Solution()
print(Solution.runningSum([1,2,3,4]))