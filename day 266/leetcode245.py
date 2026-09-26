class Solution:
    def minStartValue(self, nums):
        summ = 0
        minimum = 0

        for i in range(len(nums)):
            summ += nums[i]
            minimum = min(minimum, summ)

        return 1 - minimum
Solution = Solution()
print(Solution.minStartValue([-3,2,-3,4,2]))