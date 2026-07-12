class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort(reverse = True)
        if len(nums) < 3 :
            return nums[0]
        else: 
            
            return (nums[2])
Solution  = Solution()
print(Solution.thirdMax([3, 2, 1]))
print(Solution.thirdMax([1, 2]))