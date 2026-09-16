class Solution:
    def isMonotonic(self, nums):
        for i in range(0,len(nums)-2) :
            if nums[i] <= nums[i+1] and nums[i+1] <= nums[i+2]:
                return True
            elif nums[i] >= nums[i+1] and nums[i+1] >= nums[i+2]:
                return True 
            else :
                return False 
Solution = Solution()
print(Solution.isMonotonic([1,2,2,3]))