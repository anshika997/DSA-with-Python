class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0 
Solution = Solution()
print(Solution.largestPerimeter([1,2,1,10]))
print(Solution.largestPerimeter([2,1,2]))